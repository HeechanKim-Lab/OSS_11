# 주요 오픈소스 라이선스(OSS License) 비교 분석 및 선택 기준

> **[과제 3 - 선택과제]** 주요 OSS 라이선스를 비교 분석하여 `Micro-Tom Rhizosphere Amplicon Pipeline & AmpliconSight Workbench (OSS_11)` 프로젝트의 라이선스 선택 기준을 수립한 문서입니다.

---

## 1. 주요 오픈소스 라이선스 4종 비교 분석

오픈소스 라이선스는 크게 **허용적 라이선스(Permissive License)** 와 **카피레프트 라이선스(Copyleft License)** 로 구분됩니다. 본 프로젝트와 연관된 주요 생물정보학/데이터 과학 생태계(QIIME2, Bioconductor, Scikit-bio, FastAPI, React 등)에서 널리 쓰이는 4대 라이선스를 비교했습니다.

| 비교 항목 | **MIT License** | **Apache License 2.0** | **BSD 3-Clause** | **GNU GPL v3.0** |
| :--- | :---: | :---: | :---: | :---: |
| **분류** | Permissive (허용적) | Permissive (허용적) | Permissive (허용적) | Strong Copyleft (강한 카피레프트) |
| **상업적 이용** | ✅ 가능 | ✅ 가능 | ✅ 가능 | ✅ 가능 |
| **수정 및 배포** | ✅ 가능 | ✅ 가능 | ✅ 가능 | ✅ 가능 |
| **사적 이용 (Private Use)** | ✅ 가능 | ✅ 가능 | ✅ 가능 | ✅ 가능 |
| **소스코드 공개 의무 (파생물)** | ❌ 없음 (독점 SW 결합 가능) | ❌ 없음 (독점 SW 결합 가능) | ❌ 없음 | ⚠️ **있음 (전체 소스 GPLv3 공개 필수)** |
| **명시적 특허권 부여 (Patent Grant)** | ❌ 명시 조항 없음 | ✅ **명시적 특허 허여 및 보복 조항** | ❌ 명시 조항 없음 | ✅ 명시적 특허 허여 포함 |
| **변경 사항 고지 의무** | ❌ 없음 | ✅ 수정된 파일에 변경 고지 필수 | ❌ 없음 | ✅ 변경 일자 및 내역 고지 필수 |
| **성명권/보증 부인** | 저작권 및 라이선스 고지만 유지 | NOTICE 파일 및 저작권 유지 | 기여자 이름을 홍보에 무단 사용 금지 | 저작권 고지 및 라이선스 전문 유지 |
| **대표 채택 오픈소스** | React, Vue, FastAPI, Pytest, Node.js | Kubernetes, TensorFlow, Spark | Scikit-learn, NumPy, Pandas, QIIME2 | Linux Kernel (v2), R (core), Git |

---

## 2. 본 프로젝트(`OSS_11`)의 라이선스 선택 기준

### 2.1 고려한 핵심 기준 3가지
1. **학술 연구 및 산업계 확산성 (Academic & Industrial Adoption)**
   - 대학 연구실뿐만 아니라 종자 기업·농업 바이오 스타트업에서 자사 파이프라인에 부담 없이 통합할 수 있어야 함. GPLv3와 같은 강한 카피레프트는 기업의 도입 장벽을 높임.
2. **생물정보학 의존성 생태계와의 호환성 (Dependency Compatibility)**
   - 본 프로젝트가 의존하는 Python/JS 생태계(`matplotlib` - PSF/BSD 호환, `pytest` - MIT, `Chart.js` - MIT, `scikit-bio` - BSD-3)와 법적 충돌 없이 결합 가능해야 함.
3. **기여 진입 장벽 최소화 (Low Friction for Contributors)**
   - 학부생 및 대학원생 기여자가 복잡한 특허 조항이나 파일별 변경 헤더 작성 의무 없이 자유롭게 포크(Fork)하고 PR을 보낼 수 있는 간결함이 필요함.

### 2.2 최종 결정: **MIT License 채택**
- **선정 사유**: 가장 간결하고 명확한 허용적 라이선스로서 학술 논문 재현성 코드 공유와 SaaS 웹 워크벤치(`AmpliconSight`) 상용화 전환(Dual-licensing 또는 엔터프라이즈 확장) 모두에서 최고의 유연성을 제공합니다.
- **향후 전환 트리거**: 만약 향후 독자적인 미생물 생체마커 예측 알고리즘에 대한 특허 출원이 병행될 경우, 특허 분쟁 방어 조항이 포함된 **Apache License 2.0**으로 마이너 버전 업그레이드 시 전환을 검토합니다.
