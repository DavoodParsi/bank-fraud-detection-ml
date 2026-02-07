![Bank Fraud Detection ML](assets/banner.png)

# README_EN.md

# Bank Fraud Detection - Machine Learning Project

## Project Overview
This project is designed to detect fraudulent banking transactions using classical machine learning algorithms. The pipeline includes steps for exploratory data analysis (EDA), feature engineering, model training, and final evaluation. It is structured to be fully reproducible and ready for GitHub showcase or portfolio use.

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
└── README.md / README_EN.md
```

## Workflow
1. **EDA (`01_eda.ipynb`)**: Explore the dataset, visualize distributions, correlations, and class imbalance.  
2. **Feature Engineering (`02_feature_engineering.ipynb`)**: Handle missing values, encode categorical features, scale numerical features.  
3. **Modeling (`03_modeling.ipynb`)**: Train Logistic Regression and Random Forest models; evaluate performance.  
4. **Evaluation (`04_evaluation.ipynb`)**: Final evaluation using confusion matrix and ROC curve; save the best model.  

## Installation & Usage
1. Clone the repository:  
```bash
git clone https://github.com/DavoodParsi/bank-fraud-detection-ml.git
cd bank-fraud-detection-ml
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

3. Run notebooks in order:  
   - `01_eda.ipynb`  
   - `02_feature_engineering.ipynb`  
   - `03_modeling.ipynb`  
   - `04_evaluation.ipynb`  

4. View results in the `results/` folder (`confusion_matrix.png` & `roc_curve.png`).  

## Notes
- Only the **best-performing model (Random Forest)** is saved for deployment.  
- Notebooks and code are structured for **easy and error-free execution**.  
- Suitable for **GitHub showcase** and **portfolio projects**.

