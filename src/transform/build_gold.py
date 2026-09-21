from pathlib import Path
import pandas as pd
RAW=Path("data/raw"); OUT=Path("data/processed"); OUT.mkdir(parents=True,exist_ok=True)

def build():
    customers=pd.read_csv(RAW/"customers.csv",parse_dates=["join_date"])
    recharge=pd.read_csv(RAW/"recharge.csv",parse_dates=["recharge_date"])
    usage=pd.read_csv(RAW/"usage.csv",parse_dates=["usage_date"])
    complaints=pd.read_csv(RAW/"complaints.csv",parse_dates=["complaint_date"])
    r=recharge.groupby("customer_id").agg(total_recharge=("amount","sum"),recharge_count=("recharge_id","count"),last_recharge_date=("recharge_date","max")).reset_index()
    u=usage.groupby("customer_id").agg(total_data_gb=("data_used_gb","sum"),total_call_minutes=("call_minutes","sum"),total_sms=("sms_count","sum"),last_usage_date=("usage_date","max")).reset_index()
    c=complaints.groupby("customer_id").agg(complaint_count=("complaint_id","count"),resolved_complaints=("status",lambda s:(s=="Resolved").sum()),avg_resolution_days=("resolution_days","mean")).reset_index()
    gold=customers.merge(r,on="customer_id",how="left").merge(u,on="customer_id",how="left").merge(c,on="customer_id",how="left")
    numeric=["total_recharge","recharge_count","total_data_gb","total_call_minutes","total_sms","complaint_count","resolved_complaints","avg_resolution_days"]
    for col in numeric: gold[col]=gold[col].fillna(0)
    gold["avg_resolution_days"]=gold["avg_resolution_days"].round(2); gold.rename(columns={"status":"customer_status"},inplace=True)
    gold.to_csv(OUT/"customer_360.csv",index=False)
    print(f"Created {OUT/'customer_360.csv'} with {len(gold):,} rows")
if __name__=="__main__": build()
