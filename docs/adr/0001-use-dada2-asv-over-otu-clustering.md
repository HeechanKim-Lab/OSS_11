# ADR-0001: 97% OTU 클러스터링 대신 DADA2 기반 단일 염기 해상도 ASV 채택

- **상태 (Status)**: Accepted
- **결정 일자 (Date)**: 2026-10-02
- **의사결정자 (Deciders)**: `@HeechanKim-Lab`
- **관련 이슈/PR**: [#10](https://github.com/HeechanKim-Lab/OSS_11/issues/10), [#11](https://github.com/HeechanKim-Lab/OSS_11/issues/11)

---

## 1. 배경 및 문제 상황 (Context and Problem Statement)
토마토(Micro-Tom) 근권 16S rRNA 및 ITS2 앰플리콘 시퀀싱 데이터($N=110$, 5개 배치)를 병합 분석할 때, 기존의 97% 유사도 기반 OTU(Operational Taxonomic Unit) 클러스터링은 시퀀싱 에러와 실제 생물학적 단일 염기 다형성(SNP)을 구분하지 못하며, 서로 다른 시퀀싱 배치 간 독립적인 병합(Batch Merging)이 불가능한 문제가 있었습니다.

## 2. 고려한 대안들 (Considered Options)
* **대안 A: VSEARCH 97% Closed/Open-reference OTU 클러스터링**
  - 장점: 연산 속도가 빠르고 메모리 사용량이 적음.
  - 단점: 근연종 간 미세 변이 소실, 배치 간 재클러스터링 필요.
* **대안 B: Deblur**
  - 장점: 고정 에러 프로파일 기반으로 샘플별 독립 처리 가능.
  - 단점: Paired-end 병합 후 길이가 가변적인 ITS2 영역에 불리함.
* **대안 C: DADA2 기반 ASV (Amplicon Sequence Variant) 추론**
  - 장점: 배치별 에러 모델을 학습하여 단일 염기 해상도 확보, 배치 간 무결성 병합 가능.
  - 단점: 고심도 샘플에서 메모리 사용량 증가 (OOM 리스크).

## 3. 결정 내용 및 근거 (Decision Outcome)
**대안 C (DADA2 기반 ASV 추론)** 를 채택합니다. 5개 독립 시퀀싱 배치를 일관되게 통합하고 경주(GJ) vs 기장(GB) 토양 균주 수준의 차이를 식별하기 위해 ASV 해상도가 필수적입니다.

## 4. 결과 및 영향 (Consequences)
* **긍정적 영향**: 배치 간 Feature Table 병합 정합성 100% 확보 및 `decontam` 오염 제거 정밀도 향상.
* **부정적 영향 및 완화 방안**: 대규모 배치에서 발생한 OOM 이슈(#11)는 `nbases = 1e6` 상한 설정 및 청크 분할 처리로 완벽히 완화함(MTTR 2.1시간 내 해결).
