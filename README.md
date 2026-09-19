![Bank Fraud Detection ML](assets/banner.png)

# 🏦 Bank Fraud Detection using Machine Learning

A practical machine learning project for detecting potentially fraudulent bank transactions using data preprocessing, feature engineering, classification models, and model evaluation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Overview

The goal of this project is to build a binary classification model that identifies whether a bank transaction is:

- **Legitimate (`0`)**
- **Fraudulent (`1`)**

The project follows a practical machine learning workflow covering data preparation, feature engineering, model training, evaluation, and model comparison.

The main models evaluated are:

- Logistic Regression
- Random Forest

This project focuses on understanding the complete machine learning workflow and evaluating classification performance on an imbalanced transaction dataset.

---

## Dataset

The dataset contains:

* **50,000 transactions**
* **21 features**
* Target variable: `Fraud_Label`
* Binary classification target
* Imbalanced class distribution

The dataset is used for academic and portfolio training purposes. The reported results are specific to this dataset and should not be interpreted as production fraud-detection performance.

---

## Project Workflow

The project follows these main steps:

1. Data loading and exploration
2. Missing-value handling
3. Categorical feature encoding
4. Feature selection and preparation
5. Train/test splitting with stratification
6. Model training
7. Model evaluation
8. Model comparison
9. Model saving

The train/test split uses stratification to preserve the class distribution between the training and test sets.

---

## Models

### Logistic Regression

Logistic Regression is used as a baseline classification model.

### Random Forest

Random Forest is evaluated as an ensemble-based classification model.

On the available dataset, Random Forest achieved higher evaluation metrics than Logistic Regression.

---

## Evaluation Results

The models were evaluated using accuracy, precision, recall, F1-score, and ROC-AUC.

### Overall Performance

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------: | ------: |
| Logistic Regression |     0.81 |  0.8876 |
| Random Forest       |     0.99 |  0.9889 |

### Classification Metrics

#### Logistic Regression

| Class      | Precision | Recall | F1-score |
| ---------- | --------: | -----: | -------: |
| Legitimate |      0.85 |   0.88 |     0.86 |
| Fraudulent |      0.71 |   0.65 |     0.68 |

#### Random Forest

| Class      | Precision | Recall | F1-score |
| ---------- | --------: | -----: | -------: |
| Legitimate |      0.99 |   0.99 |     0.99 |
| Fraudulent |      0.98 |   0.98 |     0.98 |

Because fraud detection involves an imbalanced target, accuracy alone is not sufficient to describe model performance. Precision, recall, F1-score, and ROC-AUC provide additional evaluation perspectives.
---

## Project Structure

<pre>
bank-fraud-detection-ml/
│
├── assets/
│   └── banner.png
│
├── data/
│   └── ...
│
├── notebooks/
│   └── ...
│
├── results/
│   └── ...
│
├── src/
│   ├── evaluate.py
│   ├── preprocess.py
│   ├── models.py
│   └── models/
│       └── rf_model.pkl
│
├── README.md
└── requirements.txt
</pre>
---

## Installation

Clone the repository and install the required dependencies:

<pre>
git clone https://github.com/DavoodParsi/bank-fraud-detection-ml.git
cd bank-fraud-detection-ml
pip install -r requirements.txt
</pre>

---

## Requirements

The main libraries used in this project are:

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter

See `requirements.txt` for the complete dependency list.

---

## Key Takeaways

This project demonstrates practical machine learning skills including:

* Working with structured transaction data
* Handling categorical and numerical features
* Preparing data for classification
* Working with imbalanced datasets
* Comparing baseline and ensemble models
* Evaluating models using multiple classification metrics
* Saving a trained model for later use

---

## Limitations

This project is intended as a practical machine learning and portfolio exercise rather than a production fraud-detection system.

It does not currently cover:

* Real-time transaction processing
* Cost-sensitive threshold optimization
* Concept drift detection
* Production model monitoring
* Automated retraining pipelines
* Advanced anomaly-detection techniques
* API deployment
* Containerized deployment
* Security, compliance, and regulatory requirements

Therefore, the reported performance should be interpreted as dataset-specific evaluation results rather than evidence of production readiness.

---

## Future Improvements

Potential extensions for a more advanced version include:

* Advanced feature engineering
* Improved handling of class imbalance
* Threshold optimization based on fraud-detection costs
* Gradient boosting models
* Explainable AI techniques
* Model monitoring and drift detection
* API deployment
* Docker-based deployment

---

## Author

**Davood Parsi**

AI/ML Engineer focused on Machine Learning, Deep Learning, and Computer Vision.
