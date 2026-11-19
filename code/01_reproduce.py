"""01_reproduce.py — 발표 결과 재현 (재활 서비스 예측 연구실, 제6장)

산재보험패널 분석용 파일로 발표의 세 모델(KNN·로지스틱 회귀·의사결정나무)을
타깃 세 개(y_service·y_job·y_soc)에 대해 다시 학습하고, 혼동행렬·특이도·재현율·
정확도·균형 정확도를 출력한다. 상관관계 상위 변수도 함께 출력한다.

실행:  python 01_reproduce.py data/data_set_total_02.csv
데이터: 근로복지공단 산재보험패널조사(https://www.pswci.or.kr) 2차 코호트 5차년도 자료를
        분석용으로 가공한 파일(저장소 data/ 폴더). 공공 개방데이터 — 비상업적 이용, 출처 표시.
"""
import sys
import warnings

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings("ignore")  # 표준화 없는 로지스틱은 수렴 경고가 뜬다 (3-2 참고)

TARGETS = ["y_service", "y_job", "y_soc"]
NAMES = {"y_service": "재활 서비스", "y_job": "직업재활", "y_soc": "사회재활"}


def report(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    spec = tn / (tn + fp)
    rec = tp / (tp + fn)
    return dict(TN=tn, FP=fp, FN=fn, TP=tp,
                특이도=round(spec * 100, 2), 재현율=round(rec * 100, 2),
                정확도=round((tn + tp) / len(y_true) * 100, 2),
                균형정확도=round((spec + rec) / 2 * 100, 2))


def main(path):
    df = pd.read_csv(path)
    print(f"데이터: {df.shape[0]:,}행 × {df.shape[1]}열")
    for t in TARGETS:
        print(f"  {NAMES[t]:6s} 이용 {int(df[t].sum()):4d}명 ({df[t].mean() * 100:.1f}%)")

    # 2장: 빈칸은 0으로 채운다 (발표 결과와 같게 맞추는 조건)
    X = df.drop(columns=TARGETS + ["ID"]).fillna(0)

    print("\n[2-3] 상관관계 상위 (양수 3 · 음수 3)")
    corr = df.drop(columns=["ID"]).fillna(0).corr()
    for t in TARGETS:
        c = corr[t].drop(TARGETS)
        top = ", ".join(f"{k} {v:+.4f}" for k, v in c.sort_values(ascending=False).head(3).items())
        bot = ", ".join(f"{k} {v:+.4f}" for k, v in c.sort_values().head(3).items())
        print(f"  {NAMES[t]}: {top} | {bot}")

    print("\n[4-2] 발표 모델 아홉 개 (테스트 20%, random_state=42)")
    rows = []
    for t in TARGETS:
        X_tr, X_te, y_tr, y_te = train_test_split(X, df[t], test_size=0.2, random_state=42)
        models = {"KNN": KNeighborsClassifier(),
                  "로지스틱": LogisticRegression(),
                  "의사결정나무": DecisionTreeClassifier(random_state=0)}
        for name, m in models.items():
            m.fit(X_tr, y_tr)
            r = report(y_te, m.predict(X_te))
            rows.append(dict(타깃=NAMES[t], 모델=name, **r))
    out = pd.DataFrame(rows)
    pd.set_option("display.width", 160)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/data_set_total_02.csv")
