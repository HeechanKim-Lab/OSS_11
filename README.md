# OSS_11

C++, Python으로 작성한 기초 프로그래밍 예제와 실습 노트북을 정리한 저장소입니다.

## 구성

- C++ 조건문, 반복문, 함수 오버로딩, 클래스 예제
- Python 실행 예제
- 공학용 계산기 및 자살률 분석 Jupyter Notebook

## GitHub Actions

`.github/workflows/metrics.yml`은 PR이 병합될 때 자동으로 리드 타임을 계산합니다.

- 측정 시작: PR 생성 시각
- 측정 종료: PR 병합 시각
- 결과 단위: 초(seconds)
- 결과 위치: GitHub Actions 실행 화면의 Summary

병합되지 않고 닫힌 PR에는 워크플로가 실행되지 않습니다.