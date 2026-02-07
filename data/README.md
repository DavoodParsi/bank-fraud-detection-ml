# Bank Transactions Dataset Description

This dataset contains users' banking transactions with the goal of detecting fraudulent transactions.  
Each row represents a transaction, and the columns describe different features of the transaction.

## Columns Description

| Column | Short Description | Data Type |
|--------|-----------------|----------|
| Transaction_ID | Transaction identifier | object |
| User_ID | User identifier | object |
| Transaction_Amount | Transaction amount | float64 |
| Transaction_Type | Transaction type (purchase, withdrawal, etc.) | object |
| Timestamp | Transaction time | object |
| Account_Balance | User account balance at the time of transaction | float64 |
| Device_Type | Type of device used for the transaction | object |
| Location | Transaction location | object |
| Merchant_Category | Merchant category (online shopping, supermarket, etc.) | object |
| IP_Address_Flag | Whether the same IP address is used in multiple transactions | float64 |
| Previous_Fraudulent_Activity | Previous fraudulent activity associated with the account | float64 |
| Daily_Transaction_Count | Number of transactions performed per day | float64 |
| Avg_Transaction_Amount_7d | Average transaction amount in the last 7 days | float64 |
| Failed_Transaction_Count_7d | Number of failed transactions in the last 7 days | float64 |
| Card_Type | Card type (Visa, MasterCard, etc.) | object |
| Card_Age | Card age (time since issuance) | float64 |
| Transaction_Distance | Distance of the transaction from the user's location | float64 |
| Authentication_Method | Authentication method (OTP, fingerprint, etc.) | object |
| Risk_Score | Transaction risk score | float64 |
| Is_Weekend | Whether the transaction occurred on a weekend | float64 |
| Fraud_Label | Is the transaction fraudulent? (1 = fraud, 0 = non-fraud) | float64 |

## General Statistics

- Total transactions: 48,896  
- Total users: 8,956  
- Unique values per column vary (Transaction_Type: 4, Device_Type: 3, Location: 5, Merchant_Category: 5, IP_Address_Flag: 2, etc.)

> This dataset is intended for training and evaluating machine learning models for fraud detection.
