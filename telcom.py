import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 1. LOAD DATA
# -------------------------------
df = pd.read_csv(r"C:/Users/ANURAG PAREEK/Downloads/archive (5)/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# -------------------------------
# 2. DATA CLEANING
# -------------------------------
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# -------------------------------
# 3. FEATURE ENGINEERING (IMPORTANT - moved up)
# -------------------------------

# Customer Type
df['CustomerType'] = df['tenure'].apply(lambda x:
                                        'New' if x < 12 else
                                        'Regular' if x < 48 else
                                        'Loyal')

# Spending Level
df['SpendingLevel'] = df['MonthlyCharges'].apply(lambda x:
                                                'Low' if x < 35 else
                                                'Medium' if x < 70 else
                                                'High')

# Avg Charge
df['AvgChargePerMonth'] = df['TotalCharges'] / df['tenure'].replace(0, 1)

# -------------------------------
# 4. BASIC VISUALIZATION
# -------------------------------

sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()

sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()

sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.xticks(rotation=40)
plt.title("Payment Method vs Churn")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# -------------------------------
# 5. GROUPBY ANALYSIS
# -------------------------------
print("\n--- GROUPBY ANALYSIS ---")

print("Contract vs Churn\n", df.groupby('Contract')['Churn'].mean())
print("\nGender vs Churn\n", df.groupby('gender')['Churn'].mean())
print("\nPayment vs Churn\n", df.groupby('PaymentMethod')['Churn'].mean())
print("\nSenior Citizen vs Churn\n", df.groupby('SeniorCitizen')['Churn'].mean())

# -------------------------------
# 6. PIVOT TABLES
# -------------------------------
print("\n--- PIVOT TABLES ---")

print(pd.pivot_table(df, values='Churn', index='Contract', columns='PaymentMethod', aggfunc='mean') * 100)

print(pd.pivot_table(df, values='MonthlyCharges', index='Contract', aggfunc='mean'))

print(pd.pivot_table(df, values='tenure', index='Churn', aggfunc='mean'))

# -------------------------------
# 7. FEATURE VISUALIZATION (FIXED)
# -------------------------------

sns.barplot(x='CustomerType', y='Churn', data=df)
plt.title("Churn by Customer Type")
plt.show()

sns.barplot(x='SpendingLevel', y='Churn', data=df)
plt.title("Churn by Spending Level")
plt.show()

sns.catplot(x='CustomerType', y='Churn', hue='SpendingLevel', kind='bar', data=df)
plt.title("Churn by Customer Type & Spending Level")
plt.show()

# -------------------------------
# 8. HIGH RISK SEGMENT
# -------------------------------

high_risk = df[(df['CustomerType'] == 'New') & (df['SpendingLevel'] == 'High')]

sns.countplot(x='Churn', data=high_risk)
plt.title("High Risk Segment (New + High Spending)")
plt.show()

# -------------------------------
# 9. SORTING & RANKING
# -------------------------------

df['ChargeRank'] = df['MonthlyCharges'].rank(ascending=False)

# -------------------------------
# 10. FUNCTION (ADVANCED)
# -------------------------------

def churn_rate(column):
    return df.groupby(column)['Churn'].mean().sort_values(ascending=False)

print("\nChurn Rate by Contract\n", churn_rate('Contract'))

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Prepare data
X = df.drop(['Churn', 'customerID'], axis=1)
X = pd.get_dummies(X)
y = df['Churn']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling (IMPORTANT)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))