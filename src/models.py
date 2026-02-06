# src/en/models.py
# ==============================================
# Model Training & Selection
# ==============================================

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score


def load_data(path: str):
    """Load processed dataset"""
    df = pd.read_csv(path)
    X = df.drop("Fraud_Label", axis=1)
    y = df["Fraud_Label"]
    return X, y


def train_models(X_train, y_train):
    """Train baseline models"""
    lr = LogisticRegression(max_iter=1000)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    lr.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    return lr, rf


def evaluate(model, X_test, y_test):
    """Evaluate model using classification report and AUC"""
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, y_pred))
    print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.4f}")


def training_pipeline(data_path: str, model_output_path: str):
    """Complete training pipeline"""
    X, y = load_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    lr_model, rf_model = train_models(X_train, y_train)

    print("Logistic Regression Evaluation")
    evaluate(lr_model, X_test, y_test)

    print("Random Forest Evaluation")
    evaluate(rf_model, X_test, y_test)

    joblib.dump(rf_model, model_output_path)
    print(f"Model saved at: {model_output_path}")
