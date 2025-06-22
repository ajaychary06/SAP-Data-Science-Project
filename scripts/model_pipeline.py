import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
file_path = 'E:/SAP Procurement Analytics/data/supplier_risk_summary.csv'  # Adjust if needed
supplier_df = pd.read_csv(file_path)

# Features and target
target = 'High_Risk'
features = ['Spend', 'Delay_Days', 'Supplier_Rating', 'Total_Orders']

X = supplier_df[features]
y = supplier_df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance
importances = model.feature_importances_
feat_imp = pd.Series(importances, index=features).sort_values(ascending=False)
print("\nFeature Importances:")
print(feat_imp)

# Optional: Save model (e.g., with joblib)
# from joblib import dump
# dump(model, '../scripts/risk_model.joblib')
