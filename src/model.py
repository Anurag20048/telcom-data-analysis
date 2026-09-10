from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

TARGET = "Churn"
DROP = ["Churn", "customerID"]


def train_model(df: pd.DataFrame, random_state: int = 42):
    X = df.drop(columns=DROP, errors="ignore")
    y = df[TARGET]
    numeric = X.select_dtypes(include=["number"]).columns.tolist()
    categorical = X.select_dtypes(exclude=["number"]).columns.tolist()
    preprocessor = ColumnTransformer([
        ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), numeric),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical),
    ])
    pipeline = Pipeline([("preprocessor", preprocessor), ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state, stratify=y)
    pipeline.fit(X_train, y_train)
    pred = pipeline.predict(X_test)
    prob = pipeline.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, prob),
        "confusion_matrix": confusion_matrix(y_test, pred).tolist(),
    }
    return pipeline, metrics


def save_model(model, path: str | Path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
