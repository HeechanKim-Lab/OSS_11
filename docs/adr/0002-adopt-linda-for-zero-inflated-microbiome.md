# ADR-0002: 영과잉(Zero-Inflated) 마이크로바이옴 차등 풍부도 검정을 위한 LinDA 채택

- **상태 (Status)**: Accepted
- **결정 일자 (Date)**: 2026-10-05
- **의사결정자 (Deciders)**: `@HeechanKim-Lab`
- **관련 이슈/PR**: [#16](https://github.com/HeechanKim-Lab/OSS_11/issues/16), [#17](https://github.com/HeechanKim-Lab/OSS_11/issues/17)

---

## 1. 배경 및 문제 상황 (Context and Problem Statement)
마이크로바이옴 ASV 테이블은 데이터의 70~90%가 0으로 채워진 영과잉(Zero-inflated) 및 상대 조성비(Compositional) 특성을 가집니다. 또한 5개 배치에서 유래한 배치 효과(Batch Effect)를 랜덤 효과(Random Effect)로 보정해야 했습니다.

## 2. 고려한 대안들 (Considered Options)
* **대안 A: DESeq2 / edgeR** — RNA-seq용 음이항 분포 모델로, 영과잉 마이크로바이옴에서 위양성률(FDR)이 과도하게 높음.
* **대안 B: ANCOM-BC2** — 편향 보정이 우수하나 혼합 효과(Mixed-effect) 모델 연산 시 110개 샘플 기준 40분 이상 소요됨.
* **대안 C: LinDA (Linear Models for Differential Abundance Analysis)** — CLR 변환 후 편향 보정 선형 혼합 모델을 적용하여 ANCOM-BC 대비 100배 이상 빠르면서 FDR 통제력이 대등함.

## 3. 결정 내용 및 근거 (Decision Outcome)
**대안 C (LinDA)** 를 채택하되, 극저빈도 분류군에 의한 `lme4` Singularity 오류(#17)를 방지하기 위해 **Prevalence 10% 프리필터링**을 파이프라인 필수 전처리로 강제합니다.

## 4. 결과 및 영향 (Consequences)
* **긍정적 영향**: 차등 풍부도 분석 실행 시간을 40분에서 15초 이내로 단축하여 웹 대시보드(`AmpliconSight`) 실시간 분석 연동이 가능해짐.
