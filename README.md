# Heart Failure Mortality Prediction

## Strumenti Formali per la Bioinformatica  
**Assignment – Terza Parte**  

**Gruppo FRA**  
Alfonso Califano  
Rachele Capuano  
Francesco Di Lauro  

---

## 1. Project Overview

Heart failure is a high-mortality clinical condition caused by the heart’s inability to ensure adequate blood and oxygen supply to body tissues.

The objective of this project is to develop and evaluate Machine Learning models for the early prediction of mortality in patients affected by heart failure, using the **Heart Failure Clinical Records Dataset**.

The analysis focuses on:

- Evaluating multiple classification algorithms
- Comparing linear and non-linear approaches
- Selecting the most appropriate model based on predictive performance and clinical relevance

---

## 2. Dataset Description

The dataset contains:

- **299 patients**
- **12 clinical features**
- **1 binary target variable: `DEATH_EVENT`**

### Target Variable

- `0` → patient survived
- `1` → patient died during follow-up

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

## 3. Methodology

### 3.1 Data Processing

- Dataset loaded using **Pandas**
- Verified absence of missing values
- Feature matrix (`X`) and target vector (`y`) defined
- Train/Test split:
  - 80% training
  - 20% test
  - Fixed `random_state` for reproducibility

For scale-sensitive models (Logistic Regression and SVM), feature standardization was applied using **StandardScaler**.

Due to slight class imbalance, `class_weight="balanced"` was used where applicable.

---

### 3.2 Evaluated Models

Four classification algorithms were tested:

- **Logistic Regression**
- **Random Forest**
- **Gradient Boosting**
- **Support Vector Machine (SVM)**

The goal was to compare:

- Linear vs ensemble methods
- Performance stability on small datasets
- Sensitivity toward the clinically relevant class (`DEATH_EVENT = 1`)

---

## 4. Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision (class 1)
- Recall (class 1)
- F1-score (class 1)
- Confusion Matrix

Particular attention was given to:

> **Recall of the positive class**, since false negatives correspond to high-risk patients not correctly identified.

---

## 5. Results

| Model | Accuracy | Recall (Death) | Precision (Death) | F1-score (Death) |
|--------|----------|----------------|-------------------|------------------|
| Logistic Regression | **0.80** | **0.64** | 0.84 | **0.73** |
| SVM | 0.70 | 0.60 | 0.65 | 0.63 |
| Random Forest | 0.73 | 0.48 | 0.80 | 0.60 |
| Gradient Boosting | 0.72 | 0.48 | 0.75 | 0.59 |

The **Logistic Regression** model achieved the best overall performance.

From a clinical perspective:

- It correctly identifies **64% of patients who died**
- It achieves an overall accuracy of **80%**
- It provides the best balance between precision and recall

---

## 6. Discussion

Although ensemble models showed comparable accuracy, they demonstrated significantly lower recall for the positive class (0.48).

Given the limited dataset size (n = 299), simpler linear models proved to be more robust and less prone to overfitting.

An additional advantage of Logistic Regression is its interpretability, which is crucial in clinical contexts where transparency and explainability are essential.

Despite encouraging results, the recall value indicates that approximately 36% of high-risk patients remain undetected, highlighting the need for further improvements and validation on larger datasets.

---

## 7. Conclusion

This project demonstrates how Machine Learning techniques can support mortality risk prediction in heart failure patients using routine clinical variables.

Among the evaluated models, **Logistic Regression** emerged as the most balanced and clinically suitable solution.

Future improvements may include:

- Hyperparameter tuning
- Cross-validation
- Feature selection
- External validation on larger cohorts

---

## 9. Setup & Execution

### 9.1 Requirements

- Python 3.11 or 3.12 (recommended)
- pip



```bash

Check your Python version:
python --version

## 9. Setup & Execution

### 9.1 Requirements

- Python 3.11 or 3.12 (recommended)
- pip

git clone https://github.com/Ackermann32/heart-failure-prediction.git
cd heart-failure-prediction

Linux/macOs:

python3.11 -m venv .venv
source .venv/bin/activate

Windows:

python -m venv .venv
.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python main.py
