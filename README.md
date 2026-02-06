# README_EN.md

# Bank Fraud Detection - Machine Learning Project

## Project Overview
This project focuses on detecting fraudulent transactions using classical machine learning models. The goal is to build a structured and reproducible pipeline for exploratory data analysis, feature engineering, modeling, and evaluation, which can be used for GitHub showcase.

## Dataset
The dataset contains transaction information and related user data. It has been preprocessed and cleaned for modeling purposes.

### Columns
| Column | Description | Data Type |
|--------|-------------|-----------|
| Transaction_ID | Unique transaction identifier | object |
| User_ID | Unique user identifier | object |
| Transaction_Amount | Transaction amount | float64 |
| Transaction_Type | Transaction type (purchase, withdrawal, etc.) | object |
| Timestamp | Transaction timestamp | object |
| Account_Balance | User account balance at the transaction time | float64 |
| Device_Type | Device used for the transaction | object |
| Location | Transaction location | object |
| Merchant_Category | Merchant category (online purchase, supermarket, etc.) | object |
| IP_Address_Flag | Whether IP address is repeated for transactions | float64 |
| Previous_Fraudulent_Activity | Previous fraudulent activity for the account | float64 |
| Daily_Transaction_Count | Number of daily transactions | float64 |
| Avg_Transaction_Amount_7d | Average transaction amount over last 7 days | float64 |
| Failed_Transaction_Count_7d | Number of failed transactions over last 7 days | float64 |
| Card_Type | Card type (Visa, MasterCard, etc.) | object |
| Card_Age | Age of the card | float64 |
| Transaction_Distance | Distance of transaction from user location | float64 |
| Authentication_Method | Authentication method (OTP, fingerprint, etc.) | object |
| Risk_Score | Transaction risk score | float64 |
| Is_Weekend | Whether the transaction occurred on a weekend | float64 |
| Fraud_Label | Fraudulent transaction indicator (1 = fraud, 0 = non-fraud) | float64 |

## Project Structure
```
bank-fraud-detection-ml/
│
├── data/
│   ├── fraud_dataset_mod.csv
│   └── README.md
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   └── evaluation.py
├── results/
│   ├── confusion_matrix.png
│   └── roc_curve.png
├── requirements.txt
└── README_EN.md
```

## Workflow
1. **EDA (`01_eda.ipynb`)**: Explore data, visualize distributions, correlation, and class balance.
2. **Feature Engineering (`02_feature_engineering.ipynb`)**: Handle missing values, encode categorical features, scale numeric features.
3. **Modeling (`03_modeling.ipynb`)**: Train Logistic Regression and Random Forest classifiers; evaluate performance.
4. **Evaluation (`04_evaluation.ipynb`)**: Final evaluation using confusion matrix and ROC curve; save selected model.

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

## Notes
Only the best-performing model (Random Forest) is saved for deployment and evaluation.

