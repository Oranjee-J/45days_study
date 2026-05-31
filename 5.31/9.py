from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
import numpy as np

X, y = load_wine(return_X_y=True)

models = {
    "DecisionTree": DecisionTreeClassifier(
        random_state=42),
    "RandomForest": RandomForestClassifier(
        n_estimators=100,
        random_state=42),
    "GBDT": GradientBoostingClassifier(
        n_estimators=100,
        random_state=42),
    "XGBoost": XGBClassifier(
        n_estimators=100,
        eval_metric='mlogloss',
        random_state=42,
        verbosity=0
    ),
}

print(f"{'model':<15} {'average acc':<12} {'sd':<10}")
print("-" * 37)

best_model = None
best_score = 0

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    mean_score = scores.mean()
    std_score = scores.std()
    print(f"{name:<15} {mean_score:.4f}       {std_score:.4f}")
    
    if mean_score > best_score:
        best_score = mean_score
        best_model = name

print(f"\nbest model: {best_model}（average acc {best_score:.4f}）")