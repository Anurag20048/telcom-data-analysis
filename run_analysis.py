from pathlib import Path
from src.data import load_data, engineer_features
from src.analysis import key_metrics, churn_rate
from src.model import train_model

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

df = engineer_features(load_data(DATA))
print("\n=== TELECOM CHURN ANALYSIS ===")
for k, v in key_metrics(df).items():
    print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
print("\nChurn by contract:")
print((churn_rate(df, "Contract") * 100).round(2).to_string())
_, metrics = train_model(df)
print("\n=== MODEL EVALUATION ===")
for k, v in metrics.items():
    print(f"{k}: {v}")
