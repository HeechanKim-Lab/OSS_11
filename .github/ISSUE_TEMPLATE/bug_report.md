---
name: "Bug Report (파이프라인 오류 보고)"
about: "데이터 전처리, DADA2 디노이징 또는 통계 분석 중 발생한 오류를 보고합니다."
title: "[BUG] "
labels: ["bug"]
assignees: []
---

## 🐛 오류 설명 (Problem Description)
어떤 오류가 발생했는지 명확하고 간결하게 설명해 주세요.

## 🔬 재현 단계 (Steps to Reproduce)
1. 파이프라인 모듈 실행: `bash modules/03_dada2_denoise.sh`
2. 입력 데이터: `data/raw_fastq/`
3. 파라미터 설정: `trunc_len_f=240, trunc_len_r=160`
4. 콘솔 에러 발생 확인

## 📋 예상 동작 (Expected Behavior)
정상적으로 완료되어 생성되어야 하는 산출물 (예: `asv_table.qza`, `rep_seqs.qza` 생성)

## 💻 오류 로그 (Error Log & Traceback)
```text
[로그 또는 에러 메시지를 여기에 붙여넣으세요]
```

## ⚙️ 실행 환경 (Environment)
- OS: [e.g. macOS / Ubuntu 22.04]
- QIIME2 / R 버전: [e.g. QIIME2 2024.5 / R 4.3.2]
- 메모리 / CPU: [e.g. 32GB RAM, 8 Cores]
