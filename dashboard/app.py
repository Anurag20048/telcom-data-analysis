from pathlib import Path
import pandas as pd
import streamlit as st
from src.data import load_data, engineer_features
from src.analysis import key_metrics, churn_rate, high_risk_segment
from src.model import train_model

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

st.set_page_config(page_title="Telecom Churn Analytics", page_icon="📊", layout="wide")
st.title("📊 Telecom Customer Churn Analytics")
st.caption("EDA • Customer segmentation • Churn prediction")

df = engineer_features(load_data(DATA))
metrics = key_metrics(df)
cols = st.columns(5)
labels = [("Customers", metrics["customers"]), ("Churn Rate", f"{metrics['churn_rate']:.1%}"), ("Avg Monthly", f"${metrics['avg_monthly_charges']:.2f}"), ("Avg Tenure", f"{metrics['avg_tenure']:.1f} mo"), ("New + High Risk", metrics["high_risk_customers"])]
for c, (label, value) in zip(cols, labels):
    c.metric(label, value)

st.subheader("Churn by Contract")
contract = (churn_rate(df, "Contract") * 100).rename("Churn %")
st.bar_chart(contract)

st.subheader("Customer Segments")
seg = df.groupby(["CustomerType", "SpendingLevel"])["Churn"].mean().unstack().fillna(0) * 100
st.dataframe(seg.round(2), use_container_width=True)

st.subheader("High-Risk Segment")
risk = high_risk_segment(df)
st.write(f"New customers with high spending: **{len(risk):,}**")
if len(risk):
    st.dataframe(risk[["customerID", "tenure", "MonthlyCharges", "Contract", "Churn"]].head(25), use_container_width=True)

with st.expander("Model evaluation"):
    _, model_metrics = train_model(df)
    st.json({k: v for k, v in model_metrics.items() if k != "confusion_matrix"})
    st.write("Confusion matrix")
    st.dataframe(pd.DataFrame(model_metrics["confusion_matrix"], index=["Actual No", "Actual Yes"], columns=["Pred No", "Pred Yes"]))
