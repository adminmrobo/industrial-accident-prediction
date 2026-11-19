"""02_imbalance.py — 불균형 보완과 기준선 (재활 서비스 예측 연구실, 제5장·4-4)

1) 표준화·클래스 가중치·랜덤 포레스트를 더한 모델 비교
2) 재활 서비스(y_service)에 복제 오버샘플링 · SMOTE(직접 구현) · 클래스 가중치 비교
3) 기준선(임계값)을 옮기며 재현율·특이도·정밀도 보기
4) 5겹 교차검증 (표준화 + 가중치 로지스틱)

실행:  python 02_imbalance.py data/data_set_total_02.csv
"""
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings("ignore")
TARGETS = ["y_service", "y_job", "y_soc"]


def scores(y, p):
    tn, fp, fn, tp = confusion_matrix(y, p).ravel()
    spec, rec = tn / (tn + fp), tp / (tp + fn)
    return dict(재현율=round(float(rec) * 100, 2), 특이도=round(float(spec) * 100, 2),
                정확도=round(float(tn + tp) / len(y) * 100, 2), 균형정확도=round(float(rec + spec) / 2 * 100, 2))


def smote(A, y, k=5, seed=0):
    """적은 쪽(1) 점과 그 이웃 사이 선분 위에 새 점을 만들어 양쪽 수를 맞춘다."""
    rng = np.random.default_rng(seed)
    mi = np.where(y == 1)[0]
    need = int((y == 0).sum() - len(mi))
    _, nb = NearestNeighbors(n_neighbors=k + 1).fit(A[mi]).kneighbors(A[mi])
    base = rng.choice(len(mi), need)
    other = nb[base, rng.integers(1, k + 1, need)]
    lam = rng.random((need, 1))
    new = A[mi][base] + lam * (A[mi][other] - A[mi][base])
    return np.vstack([A, new]), np.concatenate([y, np.ones(need)])


def main(path):
    df = pd.read_csv(path)
    X = df.drop(columns=TARGETS + ["ID"]).fillna(0)

    print("[5-3] 처방을 더한 모델 (균형 정확도 · AUC)")
    for t in TARGETS:
        X_tr, X_te, y_tr, y_te = train_test_split(X, df[t], test_size=0.2, random_state=42)
        models = {
            "KNN+표준화": make_pipeline(StandardScaler(), KNeighborsClassifier()),
            "로지스틱+표준화": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
            "로지스틱+표준화+가중치": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced")),
            "나무 깊이4+가중치": DecisionTreeClassifier(max_depth=4, class_weight="balanced", random_state=0),
            "랜덤포레스트+가중치": RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample", min_samples_leaf=5, random_state=0),
        }
        for name, m in models.items():
            m.fit(X_tr, y_tr)
            s = scores(y_te, m.predict(X_te))
            auc = roc_auc_score(y_te, m.predict_proba(X_te)[:, 1])
            print(f"  {t:9s} {name:14s} 재현율 {s['재현율']:6.2f}  균형정확도 {s['균형정확도']:6.2f}  AUC {auc:.3f}")

    print("\n[5-3] 재활 서비스 · 표준화 로지스틱에 세 처방")
    X_tr, X_te, y_tr, y_te = train_test_split(X, df["y_service"], test_size=0.2, random_state=42)
    sc = StandardScaler().fit(X_tr)
    A, B, y = sc.transform(X_tr), sc.transform(X_te), y_tr.values
    rng = np.random.default_rng(0)
    mi, ma = np.where(y == 1)[0], np.where(y == 0)[0]
    idx = np.concatenate([np.arange(len(y)), rng.choice(mi, len(ma) - len(mi))])
    runs = {
        "복제 오버샘플링": (A[idx], y[idx], None),
        "SMOTE": (*smote(A, y), None),
        "클래스 가중치": (A, y, "balanced"),
    }
    for name, (a, b, cw) in runs.items():
        m = LogisticRegression(max_iter=2000, class_weight=cw).fit(a, b)
        print(f"  {name:10s}", scores(y_te, m.predict(B)))

    print("\n[4-4] 기준선 옮기기 (재활 서비스 · 표준화 로지스틱)")
    m = LogisticRegression(max_iter=2000).fit(A, y)
    p = m.predict_proba(B)[:, 1]
    for th in (0.5, 0.4, 0.28, 0.2):
        pred = (p >= th).astype(int)
        tp = int(((pred == 1) & (y_te.values == 1)).sum())
        fp = int(((pred == 1) & (y_te.values == 0)).sum())
        s = scores(y_te, pred)
        print(f"  기준선 {th:.2f}: 재현율 {s['재현율']:6.2f}  특이도 {s['특이도']:6.2f}  정밀도 {tp / max(tp + fp, 1) * 100:6.2f}")

    print("\n[5-4] 5겹 교차검증 (표준화 + 가중치 로지스틱)")
    for t in TARGETS:
        bal, auc = [], []
        for tr, te in StratifiedKFold(5, shuffle=True, random_state=42).split(X, df[t]):
            mm = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced"))
            mm.fit(X.iloc[tr], df[t].iloc[tr])
            bal.append(scores(df[t].iloc[te], mm.predict(X.iloc[te]))["균형정확도"])
            auc.append(roc_auc_score(df[t].iloc[te], mm.predict_proba(X.iloc[te])[:, 1]))
        print(f"  {t:9s} 균형정확도 {np.mean(bal):.2f} ± {np.std(bal, ddof=1):.2f}  (최저 {min(bal):.2f} · 최고 {max(bal):.2f})  AUC {np.mean(auc):.2f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/data_set_total_02.csv")
