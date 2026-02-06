# src/en/preprocessing.py
# ==============================================
# Data Preprocessing & Feature Engineering
# ==============================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(path: str) -> pd.DataFrame:
    """Load raw dataset from CSV file"""
    return pd.read_csv(path)


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values:
    - Numerical columns: median
    - Categorical columns: mode
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features from Timestamp
    and encode categorical variables
    """
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Transaction_Hour"] = df["Timestamp"].dt.hour
    df["Transaction_Day"] = df["Timestamp"].dt.day
    df["Transaction_Month"] = df["Timestamp"].dt.month
    df["Transaction_Weekday"] = df["Timestamp"].dt.weekday

    df.drop("Timestamp", axis=1, inplace=True)

    categorical_cols = df.select_dtypes(include=["object"]).columns
    encoder = LabelEncoder()

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df


def scale_features(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """Standardize numerical features except target column"""
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    numeric_cols = numeric_cols.drop(target_col)

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df


def preprocess_pipeline(input_path: str, output_path: str):
    """Complete preprocessing pipeline"""
    df = load_data(input_path)
    df = handle_missing_values(df)
    df = feature_engineering(df)
    df = scale_features(df, target_col="Fraud_Label")

    df.to_csv(output_path, index=False)
    print(f"Processed dataset saved at: {output_path}")
