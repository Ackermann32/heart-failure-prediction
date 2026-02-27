import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

# Leggo il dataset

df = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")

X = df.drop("DEATH_EVENT", axis=1)
y = df["DEATH_EVENT"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#  modelli


models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(class_weight="balanced", max_iter=1000))
    ]),
    
    "Random Forest": RandomForestClassifier(
        random_state=42,
        class_weight="balanced",
        n_estimators=200
    ),
    
    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    ),
    
    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC(class_weight="balanced"))
    ])
}


#Training e valutazione


results = []

for name, model in models.items():
    print(f"\n===== {name} =====")
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    recall_class_1 = report["1"]["recall"]
    precision_class_1 = report["1"]["precision"]
    f1_class_1 = report["1"]["f1-score"]
    
    print("Accuracy:", round(acc, 3))
    print("Recall (classe 1 - morte):", round(recall_class_1, 3))
    print("Precision (classe 1):", round(precision_class_1, 3))
    print("F1-score (classe 1):", round(f1_class_1, 3))
    
    results.append({
        "Model": name,
        "Accuracy": acc,
        "Recall_Death": recall_class_1,
        "Precision_Death": precision_class_1,
        "F1_Death": f1_class_1
    })


# Confronto finale


results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by="Recall_Death", ascending=False)

print("\n\n=== CONFRONTO MODELLI (ordinati per Recall classe 1) ===")
print(results_df)