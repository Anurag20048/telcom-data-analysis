# 📊 Telecom Customer Churn Analysis & Prediction

> An end-to-end data analytics and machine learning project that identifies customer churn patterns, high-risk segments, and retention opportunities.

## 🎯 Project Overview

Customer churn is one of the most important challenges for subscription-based businesses. This project analyzes telecom customer data to understand **why customers leave, which customer segments are most vulnerable, and how machine learning can help prioritize retention efforts**.

The project combines data cleaning, exploratory analysis, customer segmentation, feature engineering, Logistic Regression, model evaluation, and an interactive Streamlit dashboard.

## 📌 Business Objectives

1. Measure the overall customer churn rate.
2. Identify customer characteristics associated with higher churn.
3. Compare churn across contract types, tenure, spending, and payment methods.
4. Identify high-risk customer segments.
5. Build a classification model to predict churn.
6. Translate analytical findings into practical retention recommendations.

## 🔄 Project Workflow

```text
Telecom Customer Data
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Customer Segmentation
        ↓
Churn Prediction
        ↓
Model Evaluation
        ↓
Business Recommendations
        ↓
Interactive Streamlit Dashboard
```

## 📈 Dataset

The project uses the **Telco Customer Churn** dataset containing customer demographics, subscribed services, contract information, billing details, tenure, and churn status.

The cleaned analysis dataset contains **7,032 customer records**.

## 🔎 Exploratory Analysis

The analysis investigates:

- Overall churn distribution
- Churn by contract type
- Churn by customer tenure
- Monthly-charge patterns
- Payment-method relationships
- Service adoption
- Customer segmentation
- High-risk customer groups

## 🤖 Machine Learning

A **Logistic Regression** classification pipeline is used as the baseline churn prediction model.

The pipeline includes:

- Feature preparation
- Missing-value handling
- One-hot encoding
- Feature scaling
- Stratified train/test split
- Model training
- Prediction
- Classification evaluation

### Model Evaluation

| Metric | Score |
|---|---:|
| Accuracy | 72.71% |
| Precision | 49.17% |
| Recall | 79.41% |
| F1-score | 60.74% |
| ROC-AUC | 83.33% |

Recall and ROC-AUC are included because churn prediction is an imbalanced classification problem where identifying potential churners is particularly important.

## 💡 Key Business Insights

- Month-to-month customers have the highest observed churn rate at **42.71%**.
- One-year contract customers show substantially lower churn at **11.28%**.
- Two-year contract customers show the lowest observed churn at **2.85%**.
- Customers with shorter tenure represent an important retention opportunity.
- Higher monthly charges are associated with increased churn risk in the exploratory analysis.
- The analysis identifies **829 customers** in the New + High Spending segment for targeted retention analysis.

## 💼 Business Recommendations

1. Encourage month-to-month customers to move toward longer-term contracts.
2. Strengthen onboarding and retention programs for newer customers.
3. Prioritize high-value customers showing churn risk.
4. Investigate payment and service friction among high-risk groups.
5. Use model predictions to prioritize retention activity rather than treating them as guaranteed outcomes.

## 📊 Dashboard

The Streamlit dashboard brings the analysis together through:

- Churn KPIs
- Customer segmentation
- Contract analysis
- Monthly-charge analysis
- Churn visualizations
- Model evaluation metrics
- Interactive filtering

![Dashboard Preview](assets/dashboard-preview.svg)

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Testing | Pytest |
| Version Control | Git / GitHub |

## 📁 Project Structure

```text
telcom-data-analysis/
├── assets/
│   ├── architecture.svg
│   └── dashboard-preview.svg
├── dashboard/
│   └── app.py
├── src/
│   ├── analysis.py
│   ├── data.py
│   └── model.py
├── tests/
│   └── test_analysis.py
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── run_analysis.py
├── telcom.py
├── requirements.txt
└── README.md
```

## ▶️ Run the Project

### Clone the repository

```bash
git clone https://github.com/Anurag20048/telcom-data-analysis.git
cd telcom-data-analysis
```

### Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the analysis

```bash
python run_analysis.py
```

### Run tests

```bash
pytest -q
```

### Launch the dashboard

```bash
streamlit run dashboard/app.py
```

## 🧪 Skills Demonstrated

- Data cleaning and validation
- Exploratory Data Analysis
- Feature engineering
- Customer segmentation
- Classification modeling
- Model evaluation
- Business analytics
- Data visualization
- Dashboard development
- Python and Scikit-learn
- Translating model output into business recommendations

## 🔮 Future Enhancements

- Compare Logistic Regression with Random Forest and XGBoost
- Add cross-validation and hyperparameter tuning
- Add model explainability
- Add SQL-based analysis
- Expand dashboard analytics
- Deploy the Streamlit dashboard

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed improvement.

## 📄 License

See the `LICENSE` file for licensing information.

## 👤 Author

**Anurag Pareek**

- GitHub: https://github.com/Anurag20048
