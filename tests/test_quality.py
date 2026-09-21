import pandas as pd
from pathlib import Path
RAW=Path("data/raw")
def test_customer_ids_are_unique(): assert pd.read_csv(RAW/"customers.csv")["customer_id"].is_unique
def test_child_records_have_valid_customers():
    ids=set(pd.read_csv(RAW/"customers.csv")["customer_id"])
    for name in ["recharge.csv","usage.csv","complaints.csv"]: assert set(pd.read_csv(RAW/name)["customer_id"]).issubset(ids)
def test_usage_values_are_non_negative():
    df=pd.read_csv(RAW/"usage.csv"); assert (df["data_used_gb"]>=0).all() and (df["call_minutes"]>=0).all() and (df["sms_count"]>=0).all()
