# Heart Failure Mortality Prediction

## Project Overview

Cardiovascular diseases are the leading cause of death worldwide.  
This project aims to develop a Machine Learning model for the early detection of mortality risk in patients affected by heart failure.

The task consists of predicting the binary outcome **DEATH_EVENT** using 12 clinical features.

---

## Dataset

**Name:** Heart Failure Clinical Records Dataset  
**Samples:** 299 patients  
**Features:** 12 clinical variables  
**Target variable:** DEATH_EVENT (0 = survival, 1 = death)

### Clinical Features

- age
- anaemia
- creatinine_phosphokinase
- diabetes
- ejection_fraction
- high_blood_pressure
- platelets
- serum_creatinine
- serum_sodium
- sex
- smoking
- time

The dataset does not contain missing values.

---

## Methodology

### 1. Data Preprocessing
- Dataset loaded using Pandas
- Checked for missing values
- Split into features (X) and target (y)
- Train/Test split (80% / 20%)

### 2. Model Selection

A **Random Forest Classifier** was used due to:
- Robustness to overfitting
- Good performance on tabular clinical data
- Minimal preprocessing requirements

### 3. Model Training

The model was trained on the training set and evaluated on the test set.

---

## Evaluation Metrics

The following metrics were computed:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Particular attention was given to **Recall for the positive class (DEATH_EVENT = 1)**, as minimizing false negatives is crucial in medical diagnosis.

---

## Results

(Insert here your actual results)

Example:

- Accuracy: 0.85
- Precision: 0.82
- Recall: 0.78
- F1-score: 0.80

The model demonstrates good predictive capability for early mortality detection.

---

## Feature Importance

Feature importance analysis was performed using the Random Forest model.

The most relevant predictors include:

- serum_creatinine
- ejection_fraction
- time
- age

These variables are clinically coherent with known heart failure risk factors.

---

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/heart-failure-prediction.git
cd heart-failure-prediction
