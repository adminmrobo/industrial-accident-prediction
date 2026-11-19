"""00_make_demo_data.py — 연습용 가짜 데이터 만들기

산재보험패널 자료를 아직 받지 못했을 때, 01·02 코드가 돌아가는지만 확인하려고 만드는
**가짜(모의) 데이터**다. 열 이름과 값의 범위만 분석용 파일과 비슷하게 맞췄고, 사람도 숫자도 실제가 아니다.
이 파일로 나온 성적은 해설의 숫자와 같지 않으며, 어떤 해석에도 쓰면 안 된다.

실행:  python 00_make_demo_data.py data/demo.csv
"""
import os
import sys

import numpy as np
import pandas as pd

rng = np.random.default_rng(2024)
N = 2728
COLS = ["work_type", "acc_type", "injury_type", "Injury_part", "period", "acc_year", "hire_date", "gender", "age_type",
        "edu_type", "area_type", "disa_type0", "disa_type1", "disa_type2", "emp_type0", "emp_type1", "emp_type2",
        "emp_type3", "fin_edu", "fin_edu1", "marry", "disa_reg", "disa_type00", "lice_type", "lice_sum", "add_com",
        "com_sum", "add_insure", "ability", "week_work1", "week_work2", "week_rest", "health_stat01", "health_stat02",
        "hopital_visit0", "hopital_visit1", "disa_const01", "disa_const02", "dia_help_need", "dia_help_per", "exr_week",
        "sleep_hour", "smoke", "alchol", "dem_effect", "socia_lev", "satisfy_01", "satisfy_02", "satisfy_03",
        "satisfy_04", "satisfy_05", "satisfy_06", "satisfy_total", "work_wage01", "work_wage_sum", "pension01_sum",
        "pension02_sum", "pension03_sum", "pension04_sum", "pension05_sum", "fin_income", "est_income", "etc_income",
        "total_income01", "total_income02", "family_num", "family_income", "family_consume"]
MONEY = {"com_sum", "work_wage_sum", "pension01_sum", "pension02_sum", "pension03_sum", "pension04_sum",
         "pension05_sum", "fin_income", "est_income", "etc_income", "total_income01", "total_income02",
         "family_income", "family_consume"}

df = pd.DataFrame({"ID": np.arange(1, N + 1)})
for c in COLS:
    df[c] = np.round(rng.gamma(1.2, 1500, N)) if c in MONEY else rng.integers(1, 7, N)
# 이용 여부: 요양기간이 길수록 조금 더 이용하도록 만든 가짜 규칙 (실제 관계가 아님)
p_job = 1 / (1 + np.exp(-(-2.4 + 0.25 * df["period"])))
p_soc = 1 / (1 + np.exp(-(-2.6 + 0.30 * df["period"])))
df["y_job"] = (rng.random(N) < p_job).astype(int)
df["y_soc"] = (rng.random(N) < p_soc).astype(int)
df["y_service"] = ((df["y_job"] + df["y_soc"]) > 0).astype(int)
df = df[["y_service", "y_job", "y_soc", "ID"] + COLS]

out = sys.argv[1] if len(sys.argv) > 1 else "data/demo.csv"
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
df.to_csv(out, index=False)
print(f"가짜 데이터 저장: {out} ({df.shape[0]}행 × {df.shape[1]}열) — 연습용, 해석 금지")
