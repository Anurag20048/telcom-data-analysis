import pandas as pd


def churn_rate(df: pd.DataFrame, column: str) -> pd.Series:
    return df.groupby(column)["Churn"].mean().sort_values(ascending=False)


def high_risk_segment(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["CustomerType"] == "New") & (df["SpendingLevel"] == "High")].copy()


def key_metrics(df: pd.DataFrame) -> dict:
    return {
        "customers": int(len(df)),
        "churn_rate": float(df["Churn"].mean()),
        "avg_monthly_charges": float(df["MonthlyCharges"].mean()),
        "avg_tenure": float(df["tenure"].mean()),
        "high_risk_customers": int(len(high_risk_segment(df))),
    }
