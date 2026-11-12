# 🔒 패키지 배포, 컨테이너 검증 및 보안 스캔(Dependabot / Audit) 리포트

> **[과제 6]** `@heechankim-lab/oss-11` npm 패키지 버전 업데이트(`1.0.0` → `1.0.1`), Docker 컨테이너 자동 빌드/검증, 그리고 Dependabot 및 `npm audit` 보안 스캔 자동화 결과 보고서입니다.

---

## 1. NPM 패키지 배포 및 버전 업데이트 이력 (`1.0.0` → `1.0.1`)

- **패키지명**: `@heechankim-lab/oss-11`
- **레지스트리**: GitHub Packages (`https://npm.pkg.github.com`)
- **버전 업데이트 내역**:
  - `v1.0.0`: Casava 1.8 FASTQ 레코드 검증기 및 SHA-256 결정론적 버킷 함수 최초 릴리즈
  - `v1.0.1`: 빈 문자열 입력 예외 처리 강화 및 자가진단(`selfTest()`) CLI 헬퍼 추가
- **자동 배포 워크플로우**: [`.github/workflows/publish_packages_docker.yml`](../.github/workflows/publish_packages_docker.yml)

---

## 2. Docker 컨테이너 이미지 빌드 및 로컬 헬스체크 검증

- **이미지 레지스트리**: `ghcr.io/heechankim-lab/oss_11:1.0.1` (`latest` 태그 동시 부여)
- **컨테이너 사양**: `python:3.10-slim` 기반 경량 이미지, `8080` 포트 노출, 15초 주기 내장 `HEALTHCHECK` 적용
- **CI 내 컨테이너 기동 및 `/health.json` 검증 결과**:
  ```json
  {
    "status": "UP",
    "service": "AmpliconSight Web Workbench & API",
    "version": "1.0.1",
    "cohort": "Micro-Tom Rhizosphere Amplicon (N=110)",
    "slo_metrics": {
      "error_rate_pct": 0.4,
      "p95_latency_ms": 88.5,
      "canary_stage": "100%"
    }
  }
  ```

---

## 3. Dependabot 정책 및 보안 취약점 스캔 결과

1. **Dependabot 구성 ([`.github/dependabot.yml`](../.github/dependabot.yml))**:
   - **대상 생태계**: `pip`, `npm`, `github-actions`, `docker` (4종 전체 커버)
   - **스케줄**: 매주 월요일 09:00 KST 자동 스캔
   - **그룹화(Grouping)**: `minor` 및 `patch` 업데이트를 단일 PR 그룹(`python-minor-patch`, `npm-minor-patch`)으로 묶어 PR 노이즈 방지
2. **자동 보안 감사 (`npm audit`) 결과**:
   - **Critical**: `0`건 / **High**: `0`건 / **Moderate**: `0`건 / **Low**: `0`건
   - 런타임 외부 의존성 제로(Zero-dependency Node `crypto` 표준 내장 모듈 활용) 설계를 통해 공급망 공격(Supply-chain vulnerability) 표면을 원천 제거했습니다.
