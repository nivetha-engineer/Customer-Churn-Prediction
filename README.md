# customer-churn-classification
End-to-end Machine Learning project for predicting telecom customer churn using data preprocessing, feature engineering, multiple classification models, hyperparameter tuning, and ROC-AUC evaluation.

## Project Overview

Customer churn prediction is a machine learning classification project that predicts whether a telecom customer is likely to leave the company based on customer demographics, account information, and subscribed services.

This project demonstrates a complete end-to-end machine learning workflow, including data preprocessing, feature engineering, model training, hyperparameter tuning, and model evaluation.

---

## Dataset

Dataset: Telco Customer Churn Dataset

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Project Workflow

- Data Loading
- Data Cleaning
- Missing Value Handling
- Data Type Conversion
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Train-Test Split
- Model Training
- Hyperparameter Tuning using RandomizedSearchCV
- Model Evaluation
- ROC Curve Comparison

---

## Machine Learning Models Used

- Logistic Regression
- Ridge Classifier
- Lasso Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- XGBoost Classifier

---

## Hyperparameter Tuning

RandomizedSearchCV was used to optimize model performance.

---

## Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- ROC-AUC Score
- ROC Curve

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

## Project Structure

```
Customer-Churn-Prediction/
│
├── Customer Churn Prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── README.md
└── requirements.txt
```

---

## Key Learning Outcomes

- Data preprocessing techniques
- Feature encoding
- Feature scaling
- Classification algorithms
- Hyperparameter tuning
- Model evaluation using ROC-AUC
- Comparing multiple machine learning models

---

## Results

The performance of multiple machine learning models was evaluated on the test dataset.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|---------:|----------:|--------:|---------:|---------:|
| Logistic Regression | **82.19%** | 68.71% | **60.05%** | **64.09%** | **0.7510** |
| Ridge Classifier | **82.40%** | **70.76%** | 57.10% | 63.20% | 0.7431 |
| SVC | 81.05% | 69.92% | 49.87% | 58.22% | 0.7107 |
| Random Forest | 80.77% | 68.75% | 50.13% | 57.98% | 0.7096 |
| XGBoost | 78.57% | 62.12% | 48.79% | 54.65% | 0.6904 |

**Best Overall Model:** Logistic Regression achieved the best balance between Accuracy, F1-Score, and ROC-AUC, making it the most suitable model for this customer churn prediction task.

## Future Improvements

- Deploy the model using Streamlit or Flask
- Perform advanced feature engineering
- Handle class imbalance using SMOTE
- Build an interactive dashboard

---

## Conclusion

- Built an end-to-end machine learning pipeline to predict customer churn.
- Performed data cleaning, preprocessing, feature encoding, and feature scaling.
- Trained and evaluated multiple classification models, including Logistic Regression, Ridge, Lasso, Random Forest, SVM, and XGBoost.
- Applied RandomizedSearchCV for hyperparameter tuning to improve model performance.
- Evaluated the models using Accuracy, ROC-AUC, ROC Curve, Classification Report, and Confusion Matrix.
- This project demonstrates how machine learning can help telecom companies identify customers who are likely to churn and support customer retention strategies.

## Author

**Nive**

Aspiring Data Scientist

GitHub:
https://github.com/nivetha-engineer
