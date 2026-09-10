from pathlib import Path
import pandas as pd


def load_data(path: str | Path) -> pd.DataFrame:
    """Load and clean the Telco churn dataset from a portable path."""
    df = pd.read_csv(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna().drop_duplicates().copy()
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["CustomerType"] = out["tenure"].apply(lambda x: "New" if x < 12 else ("Regular" if x < 48 else "Loyal"))
    out["SpendingLevel"] = out["MonthlyCharges"].apply(lambda x: "Low" if x < 35 else ("Medium" if x < 70 else "High"))
    out["AvgChargePerMonth"] = out["TotalCharges"] / out["tenure"].replace(0, 1)
    out["ChargeRank"] = out["MonthlyCharges"].rank(ascending=False)
    return out
