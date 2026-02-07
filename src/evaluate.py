# src/en/evaluation.py
# ==============================================
# Final Model Evaluation & Visualization
# ==============================================

import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc, classification_report


def load_model(path: str):
    """Load trained model"""
    return joblib.load(path)


def load_data(path: str):
    """Load evaluation dataset"""
    df = pd.read_csv(path)
    X = df.drop("Fraud_Label", axis=1)
    y = df["Fraud_Label"]
    return X, y


def plot_confusion_matrix(y_true, y_pred, save_path: str):
    """Plot and save confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.savefig(save_path)
    plt.show()


def plot_roc_curve(y_true, y_prob, save_path: str):
    """Plot and save ROC curve"""
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.savefig(save_path)
    plt.show()


def evaluation_pipeline(model_path, data_path, cm_path, roc_path):
    """Complete evaluation pipeline"""
    model = load_model(model_path)
    X, y = load_data(data_path)

    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:, 1]

    print(classification_report(y, y_pred))
    plot_confusion_matrix(y, y_pred, cm_path)
    plot_roc_curve(y, y_prob, roc_path)
