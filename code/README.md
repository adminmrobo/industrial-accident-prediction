# code — 재현 코드

| 파일 | 하는 일 | 해설 |
|---|---|---|
| `00_make_demo_data.py` | 자료를 받기 전 연습용 **가짜 데이터** 만들기 (같은 열 이름, 무작위 값 — 해석 금지) | 6-1 |
| `01_reproduce.py` | 이용률, 상관관계 상위, 발표 모델 아홉 개(KNN·로지스틱·의사결정나무 × 타깃 3)의 혼동행렬과 지표 | 2~4장 |
| `02_imbalance.py` | 표준화·클래스 가중치·랜덤 포레스트, 복제·SMOTE(직접 구현)·가중치, 기준선 옮기기, 5겹 교차검증 | 4-4 · 5장 |
| `variable_map.csv` | 분석용 이름 ↔ 원래 변수명(발표 9~11쪽 표) ↔ 한글 이름 | 2-1 · 6-1 |
| `requirements.txt` | pandas · numpy · scikit-learn | — |

```bash
# (자료가 아직 없으면) 연습용 가짜 데이터로 돌아가는지만 확인
python code/00_make_demo_data.py data/demo.csv

pip install -r code/requirements.txt
python code/01_reproduce.py data/data_set_total_02.csv
python code/02_imbalance.py data/data_set_total_02.csv
```

## 데이터

`data/data_set_total_02.csv`(2,728행 × 72열)는 근로복지공단 [산재보험패널조사](https://www.pswci.or.kr) 2차 코호트 5차년도 자료(pswci_05_wide)를 발표자가 가공한 분석용 파일입니다. 공공 개방데이터로 **비상업적 이용이 가능**하며, 쓸 때는 출처(근로복지공단 산재보험패널조사)를 밝혀 주세요.

- 빈칸은 모두 0으로 채웁니다 (발표 결과와 같게 맞추는 조건, 해설 2-1 참고).
- 나누기는 `test_size=0.2, random_state=42`입니다. 이 조건에서 KNN 결과가 발표 값과 소수 둘째 자리까지 같습니다.
- 표준화 없는 로지스틱 회귀는 수렴 경고가 뜨며, 라이브러리 판에 따라 발표 값과 한두 명 차이가 납니다.
- 다른 연도·코호트로 넓힐 때는 `variable_map.csv`대로 원 자료에서 변수를 골라 이름을 바꿉니다.
- `00_make_demo_data.py`는 실제 결과를 미리 보여 주지 않고 코드만 연습시킬 때 쓰는 가짜 데이터입니다.
