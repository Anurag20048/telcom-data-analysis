from pathlib import Path
from src.data import load_data, engineer_features
from src.analysis import key_metrics, high_risk_segment

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "WA_Fn-UseC_-Telco-Customer-Churn.csv"


def test_dataset_loads_from_repo_path():
    df = load_data(DATA)
    assert len(df) > 7000
    assert df["Churn"].isin([0, 1]).all()


def test_feature_engineering_creates_expected_columns():
    df = engineer_features(load_data(DATA))
    for column in ["CustomerType", "SpendingLevel", "AvgChargePerMonth", "ChargeRank"]:
        assert column in df.columns


def test_metrics_and_risk_segment_are_valid():
    df = engineer_features(load_data(DATA))
    metrics = key_metrics(df)
    assert 0 <= metrics["churn_rate"] <= 1
    risk = high_risk_segment(df)
    assert (risk["CustomerType"] == "New").all()
    assert (risk["SpendingLevel"] == "High").all()
