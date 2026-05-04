# Diabetes Risk Predictor

A machine learning web application that predicts diabetes risk based on patient health and demographic data.

## Project Overview

This project was completed in three phases:
- **Phase 1:** Data collection, processing, and exploratory data analysis
- **Phase 2:** Predictive modeling using four ML algorithms
- **Phase 3:** Flask web application for live model inference

## Dataset

- **Source:** [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) via Kaggle
- **Size:** 100,000 rows, 9 features
- **Target Variable:** Diabetes (binary: 0 = No, 1 = Yes)
- **Note:** The dataset is not included in this repository. Download it from Kaggle and place `diabetes_prediction_dataset.csv` in the root directory before running the notebooks.

## Models Trained

| Algorithm | ROC-AUC | F1 (Diabetic) |
|-----------|---------|----------------|
| KNN | 0.916 | 0.67 |
| Logistic Regression | 0.958 | 0.69 |
| Random Forest | 0.962 | 0.78 |
| XGBoost | 0.976 | 0.81 |

XGBoost was selected as the final model.

## Setup and Running

### Step 1: Clone the repository
```bash
git clone https://github.com/Cashstu/diabetes-risk-predictor
cd diabetes-risk-predictor
```

### Step 2: Install dependencies
```bash
pip install flask xgboost joblib numpy scikit-learn pandas matplotlib seaborn imbalanced-learn jupyter
```

### Step 3: Download the dataset
Download `diabetes_prediction_dataset.csv` from [Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) and place it in the root directory.

### Step 4: Generate the trained model
Open and run `Phase2_Cashel_Stuger.ipynb` in Jupyter. The final cell will save `xgb_model.pkl` to the root directory. This file is required to run the web app.

### Step 5: Run the web app
```bash
cd diabetes_app
python app.py
```
Open your browser and go to `http://127.0.0.1:5000`

### Input Fields

| Field | Description |
|-------|-------------|
| Gender | 0 = Female, 1 = Male, 2 = Other |
| Age | Patient age in years |
| Hypertension | 0 = No, 1 = Yes |
| Heart Disease History | 0 = No, 1 = Yes |
| BMI | Body Mass Index |
| HbA1c Level | Glycated hemoglobin level |
| Blood Glucose Level | Blood glucose in mg/dL |
| Smoking History | 0 = Current, 1 = Ever, 2 = Former, 3 = Never, 4 = Not Current, 5 = Unknown |

# 

Cashel Stuger  
COMP 399-004 - Data Intensive Computing  
Bridgewater State University