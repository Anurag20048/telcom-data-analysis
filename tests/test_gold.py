import pandas as pd
from pathlib import Path
def test_gold_one_row_per_customer():
    df=pd.read_csv(Path("data/processed/customer_360.csv")); assert df["customer_id"].is_unique; assert len(df)==1000
def test_gold_metrics_are_non_negative():
    df=pd.read_csv(Path("data/processed/customer_360.csv"))
    for col in ["total_recharge","total_data_gb","total_call_minutes","total_sms","complaint_count"]: assert (df[col]>=0).all()
