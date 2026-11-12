#!/usr/bin/env python3
"""
validate_prd.py — lean-prd 스킬이 생성한 docs/prd/ 의 *형식*을 검사한다.

사용법:
    python3 validate_prd.py docs/prd            # 검사
    python3 validate_prd.py docs/prd --strict   # 경고(WARN)도 실패로 처리

검사하는 것 (형식):
    - 12개 파일 존재, 파일명 규격
    - 각 파일의 첫 헤딩과 메타 블록(제품/버전/최종 수정/관련 가설)
    - 파일별 필수 헤딩 (references/prd-section-guide.md 와 동일)
    - 템플릿 자리표시자({{…}})와 TODO 잔존 여부
    - 가설 ID(H#)가 01에 정의되고 05·06·09에서 참조되는지
    - 03의 In 항목에 가설 ID 또는 명시된 예외 사유가 있는지
    - 08 계층별 표의 6열이 비어 있지 않은지
    - 09 마일스톤 블록(MS0~MS3)에 검증 가설·숫자 종료 조건이 있는지
    - 09의 No-Go가 가리키는 Pivot 옵션 P#가 10에 존재하는지
    - 10의 Pivot 트리거에 숫자가 있는지
    - 11에 Cycle 0 블록과 검토 메모 섹션이 있는지

검사하지 않는 것 (내용):
    - 03 성공 기준 · 05 목표치 · 06 임계값 · 09 종료 조건의 숫자가 서로 같은지
    - 기술 스택 근거가 타당한지, 가격이 맞는지
    - 가설이 정말 "가장 위험한" 것인지
  → 이것들은 SKILL.md 4단계(교차 참조 검사)에서 사람이/모델이 확인한다.

ID 네임스페이스: 가설 H#, 지표 M#, 실험 E#, 마일스톤 MS#, Pivot 옵션 P#, 트리거 T#.
  (지표와 마일스톤을 둘 다 M#로 쓰면 "M2 ≥ 50%"가 지표인지 마일스톤인지 읽을 수 없어 분리한다.)

학생 확장 지점: 파일 하단 CUSTOM_RULES 에 함수를 추가한다 (과제 Part A-3).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 규격 정의
# ---------------------------------------------------------------------------

FILES = [
    "00-overview.md",
    "01-problem-and-hypotheses.md",
    "02-target-customer.md",
    "03-solution-and-mvp.md",
    "04-requirements.md",
    "05-metrics.md",
    "06-experiment-plan.md",
    "07-team.md",
    "08-tech-stack.md",
    "09-milestones.md",
    "10-risks-and-pivot.md",
    "11-bml-log.md",
]

REQUIRED_HEADINGS: dict[str, list[str]] = {
    "00-overview.md": ["## 1. 한 줄 정의", "## 2. 비전과 현재 단계", "## 3. Lean Canvas 요약", "## 4. 문서 맵"],
    "01-problem-and-hypotheses.md": ["## 1. 문제 정의", "## 2. 현재 대안과 한계", "## 3. 가설 목록", "## 4. 가장 위험한 가정 순위"],
    "02-target-customer.md": ["## 1. 고객 세그먼트", "## 2. 얼리어답터 페르소나", "## 3. 접근 채널과 첫 10명"],
    "03-solution-and-mvp.md": ["## 1. 솔루션 개요", "## 2. MVP 유형과 선택 이유", "## 3. MVP 범위 (In / Out)", "## 4. MVP 성공 기준"],
    "04-requirements.md": ["## 1. 사용자 스토리", "## 2. 기능 요구사항", "## 3. 비기능 요구사항", "## 4. 우선순위 (MoSCoW)"],
    "05-metrics.md": ["## 1. North Star Metric", "## 2. AARRR 지표", "## 3. Actionable vs Vanity", "## 4. 측정 방법과 이벤트"],
    "06-experiment-plan.md": ["## 1. 실험 우선순위", "## 2. 실험 설계", "## 3. 판단 기준", "## 4. 일정과 샘플"],
    "07-team.md": ["## 1. 역할과 책임", "## 2. 마일스톤별 팀 구성", "## 3. 채용 / 외주 우선순위", "## 4. 의사결정 규칙"],
    "08-tech-stack.md": ["## 1. 아키텍처 개요", "## 2. 계층별 스택", "## 3. 분석 · 실험 · Feature Flag", "## 4. 지금 하지 않을 것"],
    "09-milestones.md": ["## 1. 마일스톤 개요", "## 2. 마일스톤 상세", "## 3. GitHub 매핑", "## 4. 일정"],
    "10-risks-and-pivot.md": ["## 1. 리스크 레지스터", "## 2. Pivot 트리거", "## 3. 사전 정의된 Pivot 옵션", "## 4. Kill 조건"],
    "11-bml-log.md": ["## 사이클 요약", "## 검토 메모"],
}

REQUIRED_LAYERS_08 = ["프론트엔드", "백엔드", "데이터", "인증", "호스팅", "분석", "CI/CD"]

PLACEHOLDER_RE = re.compile(r"\{\{.*?\}\}")
TODO_RE = re.compile(r"\bTODO\b|\bTBD\b")
H_ID_RE = re.compile(r"\bH\d+\b")
M_ID_RE = re.compile(r"\bM\d+\b")
MS_ID_RE = re.compile(r"\bMS\d+\b")
P_ID_RE = re.compile(r"\bP\d+\b")
NUMBER_RE = re.compile(r"\d")

# ---------------------------------------------------------------------------
# 결과 수집
# ---------------------------------------------------------------------------


class Report:
    def __init__(self) -> None:
        self.fails: list[str] = []
        self.warns: list[str] = []
        self.passes: list[str] = []

    def fail(self, msg: str) -> None:
        self.fails.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)

    def ok(self, msg: str) -> None:
        self.passes.append(msg)


def read(prd: Path, name: str) -> str:
    p = prd / name
    return p.read_text(encoding="utf-8") if p.exists() else ""


def section(text: str, heading: str) -> str:
    """heading(예: '## 3. MVP 범위 (In / Out)') 아래부터 다음 같은 레벨 헤딩 전까지."""
    level = heading.split(" ")[0]
    lines = text.splitlines()
    out: list[str] = []
    inside = False
    for line in lines:
        if line.strip() == heading:
            inside = True
            continue
        if inside and line.startswith(level + " "):
            break
        if inside:
            out.append(line)
    return "\n".join(out)


def table_rows(text: str) -> list[list[str]]:
    """마크다운 표의 데이터 행(헤더·구분선 제외)을 셀 리스트로."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # 구분선
        rows.append(cells)
    # 첫 행은 헤더로 간주
    return rows[1:] if rows else []


# ---------------------------------------------------------------------------
# 기본 규칙
# ---------------------------------------------------------------------------


def rule_files_exist(prd: Path, r: Report) -> None:
    missing = [f for f in FILES if not (prd / f).exists()]
    if missing:
        r.fail(f"[files] 누락: {', '.join(missing)}")
    else:
        r.ok("[files] 12개 파일 존재")
    extra = sorted(p.name for p in prd.glob("*.md") if p.name not in FILES and p.name != "README.md")
    if extra:
        r.warn(f"[files] 규격 외 파일 (허용되지만 확인): {', '.join(extra)}")


def rule_header_and_meta(prd: Path, r: Report) -> None:
    for name in FILES:
        text = read(prd, name)
        if not text:
            continue
        num = name[:2]
        first = next((l for l in text.splitlines() if l.strip()), "")
        if not re.match(rf"# {num}\. ", first):
            r.fail(f"[header] {name}: 첫 줄이 '# {num}. <제목>' 형식이 아님 → '{first[:40]}'")
        head = "\n".join(text.splitlines()[:8])
        if "| 제품 |" not in head or "최종 수정" not in head:
            r.fail(f"[meta] {name}: 상단 메타 블록(제품/버전/최종 수정/관련 가설) 없음")
    r.ok("[header/meta] 검사 완료")


def rule_required_headings(prd: Path, r: Report) -> None:
    for name, heads in REQUIRED_HEADINGS.items():
        text = read(prd, name)
        if not text:
            continue
        lines = {l.strip() for l in text.splitlines()}
        for h in heads:
            if h not in lines:
                r.fail(f"[heading] {name}: 필수 헤딩 없음 → '{h}'")
    r.ok("[heading] 검사 완료")


def rule_no_placeholders(prd: Path, r: Report) -> None:
    for name in FILES:
        text = read(prd, name)
        # HTML 주석 안의 안내문은 제외
        stripped = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        ph = PLACEHOLDER_RE.findall(stripped)
        if ph:
            r.fail(f"[placeholder] {name}: 템플릿 자리표시자 {len(ph)}개 잔존 (예: {ph[0][:30]})")
        if TODO_RE.search(stripped):
            r.fail(f"[placeholder] {name}: TODO/TBD 잔존")
    r.ok("[placeholder] 검사 완료")


def rule_hypothesis_references(prd: Path, r: Report) -> None:
    t01 = read(prd, "01-problem-and-hypotheses.md")
    defined = set()
    for row in table_rows(section(t01, "## 3. 가설 목록")):
        if row and H_ID_RE.fullmatch(row[0]):
            defined.add(row[0])
    if not defined:
        r.fail("[H#] 01 §3 가설 목록 표에서 H# 를 찾지 못함")
        return
    if len(defined) < 3:
        r.warn(f"[H#] 가설이 {len(defined)}개 — 최소 가치 2 + 성장 1 권장")
    for name, label in [("05-metrics.md", "지표"), ("06-experiment-plan.md", "실험"), ("09-milestones.md", "마일스톤")]:
        refs = set(H_ID_RE.findall(read(prd, name)))
        orphan = sorted(defined - refs)
        if orphan:
            r.fail(f"[H#] {name}: 가설 {', '.join(orphan)} 가 {label}에서 참조되지 않음")
    # 정의되지 않은 H# 참조
    for name in FILES:
        refs = set(H_ID_RE.findall(read(prd, name)))
        unknown = sorted(refs - defined)
        if unknown and name != "11-bml-log.md":  # 로그는 기각된 가설 이력을 가질 수 있음
            r.warn(f"[H#] {name}: 01에 없는 가설 참조 {', '.join(unknown)}")
    r.ok(f"[H#] 가설 {len(defined)}개 정의·참조 검사 완료")


def rule_metrics_cover_hypotheses(prd: Path, r: Report) -> None:
    t01 = read(prd, "01-problem-and-hypotheses.md")
    t05 = read(prd, "05-metrics.md")
    defined = {row[0] for row in table_rows(section(t01, "## 3. 가설 목록")) if row and H_ID_RE.fullmatch(row[0])}
    rows = table_rows(section(t05, "## 2. AARRR 지표"))
    covered = set()
    for row in rows:
        covered |= set(H_ID_RE.findall(" ".join(row)))
    missing = sorted(defined - covered)
    if missing:
        r.fail(f"[M#] 05 §2 지표 표에 가설 {', '.join(missing)} 를 검증하는 지표가 없음")
    # 가설(H#)에 연결된 지표만 숫자 목표를 요구한다. Revenue처럼 "측정만" 하는 단계는 가설 열이 "—"이면 면제.
    linked = [row for row in rows if len(row) >= 8 and H_ID_RE.search(row[7])]
    no_num = [row[0] for row in linked if not NUMBER_RE.search(row[5])]
    if no_num:
        r.fail(f"[M#] 05 §2: 가설에 연결됐는데 목표(MVP) 열에 숫자가 없는 지표 → {', '.join(no_num)}")
    r.ok("[M#] 지표-가설 커버리지 검사 완료")


def rule_mvp_in_items_have_hypothesis(prd: Path, r: Report) -> None:
    t03 = read(prd, "03-solution-and-mvp.md")
    rows = table_rows(section(t03, "## 3. MVP 범위 (In / Out)"))
    if not rows:
        r.fail("[MVP] 03 §3 In/Out 표를 찾지 못함")
        return
    bad = []
    for row in rows:
        if len(row) < 3:
            continue
        feat, scope, hyp = row[0], row[1], row[2]
        note = row[3] if len(row) > 3 else ""
        if scope.lower().startswith("in"):
            if not H_ID_RE.search(hyp) and not re.search(r"측정 장치|최소 동작", note):
                bad.append(feat)
    if bad:
        r.fail(f"[MVP] 03 §3: 가설 없는 In 항목 → {', '.join(bad)} (측정 장치/최소 동작 조건이면 비고에 명시)")
    if "## 4. MVP 성공 기준" in t03 and not M_ID_RE.search(section(t03, "## 4. MVP 성공 기준")):
        r.fail("[MVP] 03 §4 성공 기준에 M# 인용 없음")
    r.ok("[MVP] In/Out 검사 완료")


def rule_tech_stack_table(prd: Path, r: Report) -> None:
    t08 = read(prd, "08-tech-stack.md")
    rows = table_rows(section(t08, "## 2. 계층별 스택"))
    if not rows:
        r.fail("[stack] 08 §2 계층별 표를 찾지 못함")
        return
    joined = " ".join(row[0] for row in rows if row)
    for layer in REQUIRED_LAYERS_08:
        if layer not in joined:
            r.fail(f"[stack] 08 §2: 계층 '{layer}' 행 없음")
    for row in rows:
        if len(row) < 6:
            r.fail(f"[stack] 08 §2: '{row[0]}' 행이 6열 미만")
            continue
        empty = [i for i, c in enumerate(row[:6]) if not c or c in ("—", "-")]
        if empty:
            r.fail(f"[stack] 08 §2: '{row[0]}' 행의 빈 열 {len(empty)}개 (근거·대안·비용·리스크는 비워 둘 수 없음)")
    if "ADR-" not in t08:
        r.warn("[stack] 08: ADR 블록 없음 (큰 결정 1개 이상 권장)")
    nots = table_rows(section(t08, "## 4. 지금 하지 않을 것"))
    if len(nots) < 3:
        r.fail(f"[stack] 08 §4 '지금 하지 않을 것' {len(nots)}개 — 최소 3개")
    r.ok("[stack] 기술 스택 표 검사 완료")


def rule_milestones(prd: Path, r: Report) -> None:
    t09 = read(prd, "09-milestones.md")
    t10 = read(prd, "10-risks-and-pivot.md")
    blocks = re.split(r"^### (MS\d)", section(t09, "## 2. 마일스톤 상세"), flags=re.M)
    # blocks = [pre, 'MS0', body, 'MS1', body, ...]
    ids = blocks[1::2]
    bodies = blocks[2::2]
    if len(ids) < 4:
        r.fail(f"[milestone] 09 §2: 마일스톤 블록 {len(ids)}개 — '### MS0 — …' ~ '### MS3 — …' 4개 필요 (M0가 아니라 MS0)")
    pivots = set(P_ID_RE.findall(section(t10, "## 3. 사전 정의된 Pivot 옵션")))
    for mid, body in zip(ids, bodies):
        if not re.search(r"검증 가설\s*:\s*.*H\d", body):
            r.fail(f"[milestone] {mid}: '검증 가설: H#' 줄 없음")
        m = re.search(r"종료 조건\s*:\s*(.*)", body)
        if not m or not NUMBER_RE.search(m.group(1)):
            r.fail(f"[milestone] {mid}: 숫자 종료 조건 없음")
        if "No-Go" not in body:
            r.fail(f"[milestone] {mid}: No-Go 분기 없음")
        else:
            refs = set(P_ID_RE.findall(body))
            unknown = sorted(refs - pivots)
            if unknown:
                r.fail(f"[milestone] {mid}: No-Go가 가리키는 {', '.join(unknown)} 가 10 §3에 없음")
    if "gantt" not in t09:
        r.warn("[milestone] 09 §4: Mermaid gantt 없음 (권장)")
    r.ok("[milestone] 마일스톤 검사 완료")


def rule_pivot_triggers_numeric(prd: Path, r: Report) -> None:
    t10 = read(prd, "10-risks-and-pivot.md")
    rows = table_rows(section(t10, "## 2. Pivot 트리거"))
    if not rows:
        r.fail("[pivot] 10 §2 트리거 표 없음")
        return
    for row in rows:
        if len(row) >= 2 and not NUMBER_RE.search(row[1]):
            r.fail(f"[pivot] 10 §2 트리거 '{row[0]}' 조건에 숫자가 없음")
    if not table_rows(section(t10, "## 3. 사전 정의된 Pivot 옵션")):
        r.fail("[pivot] 10 §3 Pivot 옵션 표 없음")
    r.ok("[pivot] Pivot 트리거·옵션 검사 완료")


def rule_bml_log(prd: Path, r: Report) -> None:
    t11 = read(prd, "11-bml-log.md")
    if not re.search(r"^## Cycle 0", t11, flags=re.M):
        r.fail("[log] 11: '## Cycle 0 — 초기 가정' 블록 없음")
    memo = section(t11, "## 검토 메모")
    if not table_rows(memo):
        r.warn("[log] 11 검토 메모가 비어 있음 — 제출 전 검토 내역을 남길 것")
    r.ok("[log] BML 로그 검사 완료")


BASE_RULES = [
    rule_files_exist,
    rule_header_and_meta,
    rule_required_headings,
    rule_no_placeholders,
    rule_hypothesis_references,
    rule_metrics_cover_hypotheses,
    rule_mvp_in_items_have_hypothesis,
    rule_tech_stack_table,
    rule_milestones,
    rule_pivot_triggers_numeric,
    rule_bml_log,
]

# ---------------------------------------------------------------------------
# 학생 확장 지점 (과제 Part A-3): 아래에 함수를 추가하고 CUSTOM_RULES 에 등록
# 예시 규칙 두 개가 주석으로 있다. 참고해서 자신만의 규칙을 최소 2개 작성할 것.
# ---------------------------------------------------------------------------


def rule_events_match(prd: Path, r: Report) -> None:
    """[Custom Rule 1] 04 §3 비기능 요구사항의 이벤트 표와 05 §4 측정 방법의 이벤트 표에 정의된 이벤트 이름이 일치하는지 검사."""
    ev_re = re.compile(r"^`([a-z][a-z0-9_]+)`$")
    rows_04 = table_rows(section(read(prd, "04-requirements.md"), "## 3. 비기능 요구사항"))
    rows_05 = table_rows(section(read(prd, "05-metrics.md"), "## 4. 측정 방법과 이벤트"))
    e04 = {m.group(1) for row in rows_04 if row for m in [ev_re.match(row[0].strip())] if m}
    e05 = {m.group(1) for row in rows_05 if row for m in [ev_re.match(row[0].strip())] if m}
    if not e04 or not e05:
        r.fail("[custom:events] 04 §3 또는 05 §4에서 `snake_case` 이벤트 표를 찾지 못함")
        return
    if e04 != e05:
        r.fail(f"[custom:events] 04/05 이벤트 불일치: 04에만 {sorted(e04 - e05)}, 05에만 {sorted(e05 - e04)}")
    else:
        r.ok(f"[custom:events] 04/05 이벤트 이름 {len(e05)}종 정확히 일치")


def rule_team_fte_and_decision_rule(prd: Path, r: Report) -> None:
    """[Custom Rule 2] 07 §1 역할 표의 FTE 열에 숫자가 있는지, 그리고 §4 의사결정 규칙에 숫자 트리거 우선 원칙이 있는지 검사."""
    t07 = read(prd, "07-team.md")
    rows = table_rows(section(t07, "## 1. 역할과 책임"))
    if not rows:
        r.fail("[custom:team] 07 §1 역할과 책임 표 없음")
        return
    for row in rows:
        if len(row) >= 4 and not NUMBER_RE.search(row[3]):
            r.fail(f"[custom:team] 07 §1 '{row[0]}' 투입(FTE) 열에 숫자가 없음")
    sec04 = section(t07, "## 4. 의사결정 규칙")
    if "트리거" not in sec04 and "10-risks-and-pivot" not in sec04:
        r.fail("[custom:team] 07 §4 의사결정 규칙에 숫자 Pivot 트리거(10-risks-and-pivot) 우선 원칙이 명시되지 않음")
    else:
        r.ok("[custom:team] 07 §1 FTE 수치 및 §4 숫자 트리거 의사결정 규칙 검사 완료")


def rule_experiment_judgment_completeness(prd: Path, r: Report) -> None:
    """[Custom Rule 3] 06 §1에 정의된 모든 실험(E#)이 06 §3 판단 기준 표에 통과/실패 숫자 및 회색 지대 처리 규칙을 갖는지 검사."""
    t06 = read(prd, "06-experiment-plan.md")
    e_re = re.compile(r"\bE\d+\b")
    defined_exps = {row[0] for row in table_rows(section(t06, "## 1. 실험 우선순위")) if row and e_re.fullmatch(row[0])}
    judgment_rows = table_rows(section(t06, "## 3. 판단 기준"))
    if not defined_exps or not judgment_rows:
        r.fail("[custom:experiment] 06 §1 또는 §3 표를 찾지 못함")
        return
    judged_exps = set()
    for row in judgment_rows:
        if len(row) < 5:
            r.fail(f"[custom:experiment] 06 §3 '{row[0] if row else '?'}' 행이 5열 미만임")
            continue
        exp_id = row[0].strip()
        judged_exps.add(exp_id)
        if not NUMBER_RE.search(row[2]) or not NUMBER_RE.search(row[3]):
            r.fail(f"[custom:experiment] 06 §3 '{exp_id}' 행의 통과/실패 임계값에 숫자가 없음")
        if len(row[4].strip()) < 5:
            r.fail(f"[custom:experiment] 06 §3 '{exp_id}' 행의 회색 지대 처리 규칙이 비어 있거나 너무 짧음")
    missing = sorted(defined_exps - judged_exps)
    if missing:
        r.fail(f"[custom:experiment] 06 §1의 실험 중 §3 판단 기준이 누락된 실험: {', '.join(missing)}")
    else:
        r.ok(f"[custom:experiment] 실험 {len(defined_exps)}종(E#) 판단 기준 및 회색 지대 규칙 검사 완료")


CUSTOM_RULES: list = [
    rule_events_match,
    rule_team_fte_and_decision_rule,
    rule_experiment_judgment_completeness,
]

# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    prd = Path(argv[1])
    strict = "--strict" in argv
    if not prd.is_dir():
        print(f"디렉터리 없음: {prd}")
        return 2

    r = Report()
    for rule in BASE_RULES + CUSTOM_RULES:
        try:
            rule(prd, r)
        except Exception as e:  # 규칙 자체의 버그가 검증을 멈추지 않도록
            r.fail(f"[internal] {rule.__name__} 실행 오류: {e}")

    print(f"validate_prd — {prd}\n")
    for m in r.fails:
        print("FAIL ", m)
    for m in r.warns:
        print("WARN ", m)
    for m in r.passes:
        print("ok   ", m)
    print(f"\n결과: FAIL {len(r.fails)} · WARN {len(r.warns)} · ok {len(r.passes)}")
    failed = bool(r.fails) or (strict and bool(r.warns))
    print("=> " + ("실패 — 위 항목을 고치고 다시 실행" if failed else "통과"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
