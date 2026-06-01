from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test) 

print("=== confusion matrix ===")
print(confusion_matrix(y_test, y_test))

print("\n=== classification report===")
print(classification_report(y_test, y_pred, target_names=target_names))

print(f"\n=== 准确率 ===")
print(f"{accuracy_score(y_test, y_pred):.4f}")

from sklearn.metrics import roc_auc_score
try:
    auc_ovr = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='macro')
    print(f"\n=== AUC (OvR) ===")
    print(f"{auc_ovr:.4f}")
except Exception as e:
    print(f"\nERROR{e}")