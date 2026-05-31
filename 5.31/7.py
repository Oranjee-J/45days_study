from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier, plot_importance
import matplotlib.pyplot as plt


X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=0
)

xgb = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    eval_metric='logloss',
    random_state=0
)
xgb.fit(X_train, y_train)

y_pred = xgb.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc)

fig, ax = plt.subplots(figsize=(10, 6))
plot_importance(xgb, max_num_features=10, ax=ax)
plt.title("XGBoost Feature Importance (Top 10)")
plt.tight_layout()
plt.savefig("xgb_feature_importance.png", dpi=100)
plt.show()