# 📐 Architecture Decision Records (기술결정기록, ADR)

본 디렉토리는 `OSS_11 (Micro-Tom Rhizosphere Amplicon Pipeline & AmpliconSight)` 프로젝트의 주요 아키텍처 및 기술적 의사결정을 기록합니다.

## ADR 목록

| ADR 번호 | 제목 | 상태 (Status) | 결정 일자 |
| :---: | :--- | :---: | :---: |
| [ADR-0000](0000-adr-template.md) | 기술결정기록(ADR) 표준 작성 템플릿 | Template | 2026-10-01 |
| [ADR-0001](0001-use-dada2-asv-over-otu-clustering.md) | 97% OTU 클러스터링 대신 DADA2 기반 단일 염기 해상도 ASV 채택 | **Accepted** | 2026-10-02 |
| [ADR-0002](0002-adopt-linda-for-zero-inflated-microbiome.md) | 영과잉(Zero-Inflated) 마이크로바이옴 차등 풍부도 검정을 위한 LinDA 채택 | **Accepted** | 2026-10-05 |
| [ADR-0003](0003-feature-flag-hash-ab-and-canary-rollback.md) | 결정론적 해시 기반 Feature Flag A/B 테스트 및 헬스체크 Canary 자동 롤백 아키텍처 | **Accepted** | 2026-10-12 |
