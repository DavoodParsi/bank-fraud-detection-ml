![Bank Fraud Detection ML](assets/banner.png)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 🏦 Bank Fraud Detection using Machine Learning

This repository contains a **Machine Learning project for detecting fraudulent bank transactions**.  
The objective is to classify transactions as **Fraudulent (1)** or **Legitimate (0)** using supervised learning techniques.

The project covers the **entire ML pipeline**, from raw and imperfect data to model evaluation and comparison.

---

## 📌 Project Overview

Financial fraud is a critical problem in modern banking systems. Manual rule-based systems are often insufficient due to evolving fraud patterns.  
Machine Learning enables automatic detection by learning complex patterns from historical transaction data.

In this project:
- A real-world–like banking dataset is analyzed
- Missing values and mixed data types are handled
- Multiple ML models are trained and evaluated
- The best-performing model is selected based on robust metrics

---
## Dataset
The dataset contains real banking transactions with multiple features related to each transaction. It has been preprocessed and cleaned for modeling purposes.

### Columns
| Column | Description | Data Type |
|--------|-------------|-----------|
| Transaction_ID | Unique transaction identifier | object |
| User_ID | Unique user identifier | object |
| Transaction_Amount | Transaction amount | float64 |
| Transaction_Type | Transaction type (purchase, withdrawal, etc.) | object |
| Timestamp | Transaction timestamp | object |
| Account_Balance | User account balance at transaction time | float64 |
| Device_Type | Device used for the transaction | object |
| Location | Transaction location | object |
| Merchant_Category | Merchant category (online, retail, etc.) | object |
| IP_Address_Flag | Flag if IP address is repeated | float64 |
| Previous_Fraudulent_Activity | Previous fraudulent activity | float64 |
| Daily_Transaction_Count | Number of daily transactions | float64 |
| Avg_Transaction_Amount_7d | Average transaction amount over last 7 days | float64 |
| Failed_Transaction_Count_7d | Number of failed transactions over last 7 days | float64 |
| Card_Type | Card type (Visa, MasterCard, etc.) | object |
| Card_Age | Age of the card | float64 |
| Transaction_Distance | Distance of transaction from user location | float64 |
| Authentication_Method | Authentication method (OTP, fingerprint, etc.) | object |
| Risk_Score | Transaction risk score | float64 |
| Is_Weekend | Whether transaction occurred on a weekend | float64 |
| Fraud_Label | Fraudulent transaction indicator (1 = fraud, 0 = non-fraud) | float64 |

## 📊 Dataset Description

- Number of samples: **50,000**
- Number of features: **21**
- Target variable: `Fraud_Label`
  - `0` → Legitimate transaction
  - `1` → Fraudulent transaction
- The dataset is **imbalanced**, reflecting real banking scenarios
- The dataset was provided for academic training purposes

### Feature Categories

- **Transaction details**  
  `Transaction_Amount`, `Transaction_Type`, `Timestamp`, `Transaction_Distance`

- **User & account information**  
  `User_ID`, `Account_Balance`, `Card_Type`, `Card_Age`

- **Behavioral & risk indicators**  
  `Daily_Transaction_Count`, `Avg_Transaction_Amount_7d`,  
  `Failed_Transaction_Count_7d`, `Previous_Fraudulent_Activity`, `Risk_Score`

- **Contextual features**  
  `Device_Type`, `Location`, `Merchant_Category`, `Authentication_Method`, `Is_Weekend`

---

## 🧹 Data Preprocessing

The original dataset was **not clean** and required multiple preprocessing steps:

- Handling missing values
- Encoding categorical variables
- Feature selection
- Train-test split with stratification

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

All preprocessing steps were applied consistently to avoid data leakage.

---

## 🧠 Models Trained

- Logistic Regression
- Random Forest Classifier

Random Forest was selected as the final model due to superior performance.

---

## 📈 Model Evaluation

### Logistic Regression

Accuracy: **0.81**  
AUC-ROC: **0.8876**

| Class | Precision | Recall | F1-score |
|------|----------|--------|----------|
| Legitimate (0) | 0.85 | 0.88 | 0.86 |
| Fraud (1) | 0.71 | 0.65 | 0.68 |

---

### Random Forest (Final Model)

Accuracy: **0.99**  
AUC-ROC: **0.9889**

| Class | Precision | Recall | F1-score |
|------|----------|--------|----------|
| Legitimate (0) | 0.99 | 0.99 | 0.99 |
| Fraud (1) | 0.98 | 0.98 | 0.98 |

✔ Random Forest significantly outperformed Logistic Regression.

---

## 📁 Project Structure

```
bank-fraud-detection-ml/
│
├── data/
│   ├── fraud_dataset_mod.csv
│   ├── fraud_dataset_processed.csv
│   └── README.md
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_evaluation.ipynb
│   └── notebook.ipynb
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   └── models/
│       └── rf_model.pkl
├── results/
│   ├── confusion_matrix.png
│   └── roc_curve.png
├── requirements.txt
└── README.md 
```

---

## ▶️ How to Run

```bash
git clone https://github.com/DavoodParsi/bank-fraud-detection-ml.git
pip install -r requirements.txt
```

---

## 🚀 Key Takeaways

- Fraud datasets are noisy and imbalanced
- Proper preprocessing is critical
- Ensemble models perform very well
- Metrics beyond accuracy are essential

---

## 👤 Author

Davood Parsi  
Machine Learning Enthusiast

---

## 📜 License

MIT License
