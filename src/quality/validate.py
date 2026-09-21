from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
SCHEMAS = {
    "customers.csv": ["customer_id","customer_name","city","state","plan","join_date","status"],
    "recharge.csv": ["recharge_id","customer_id","recharge_date","amount","payment_mode"],
    "usage.csv": ["usage_id","customer_id","usage_date","data_used_gb","call_minutes","sms_count"],
    "complaints.csv": ["complaint_id","customer_id","complaint_date","issue_type","status","resolution_days"],
}

def validate():
    failures, frames = [], {}
    for name, cols in SCHEMAS.items():
        path = RAW / name
        if not path.exists():
            failures.append(f"Missing file: {path}")
            continue
        df = pd.read_csv(path)
        frames[name] = df
        if list(df.columns) != cols: failures.append(f"{name}: schema mismatch")
        if df.empty: failures.append(f"{name}: empty dataset")
        if df[cols[0]].duplicated().any(): failures.append(f"{name}: duplicate primary keys")
        if df.isna().any().any(): failures.append(f"{name}: null values found")
    if "customers.csv" in frames:
        ids = set(frames["customers.csv"]["customer_id"])
        for child in ["recharge.csv","usage.csv","complaints.csv"]:
            if child in frames:
                bad = set(frames[child]["customer_id"]) - ids
                if bad: failures.append(f"{child}: {len(bad)} orphan customer IDs")
    if failures:
        for f in failures: print("FAIL:", f)
        raise SystemExit(1)
    print("DATA QUALITY: PASS")
    for name, df in frames.items(): print(f"{name}: {len(df):,} rows")

if __name__ == "__main__":
    validate()
    from src.quality.quality_report import run_report
    run_report()
