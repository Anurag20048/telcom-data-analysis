from pathlib import Path
import json
import pandas as pd

RAW=Path("data/raw"); OUT=Path("data/quality"); OUT.mkdir(parents=True,exist_ok=True)
RULES={
"customers.csv":["customer_id","customer_name","city","state","plan","join_date","status"],
"recharge.csv":["recharge_id","customer_id","recharge_date","amount","payment_mode"],
"usage.csv":["usage_id","customer_id","usage_date","data_used_gb","call_minutes","sms_count"],
"complaints.csv":["complaint_id","customer_id","complaint_date","issue_type","status","resolution_days"]}

def run_report():
    customers=pd.read_csv(RAW/"customers.csv"); ids=set(customers.customer_id); results=[]
    for filename, columns in RULES.items():
        df=pd.read_csv(RAW/filename); key=columns[0]
        checks={"row_count":len(df),"schema_ok":list(df.columns)==columns,
                "null_count":int(df.isna().sum().sum()),"duplicate_key_count":int(df[key].duplicated().sum())}
        checks["orphan_customer_count"]=int((~df.customer_id.isin(ids)).sum()) if "customer_id" in df else 0
        checks["status"]="PASS" if checks["schema_ok"] and checks["null_count"]==0 and checks["duplicate_key_count"]==0 and checks["orphan_customer_count"]==0 else "FAIL"
        results.append({"dataset":filename,**checks})
    report={"pipeline":"telecom-data-engineering-platform","status":"PASS" if all(x["status"]=="PASS" for x in results) else "FAIL","datasets":results}
    (OUT/"latest_quality_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    if report["status"]!="PASS": raise SystemExit(1)
    print(json.dumps(report,indent=2))

if __name__=="__main__": run_report()
