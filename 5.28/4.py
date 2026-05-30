from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores_manual = []

for fold, (train_idx, val_idx) in enumerate(kf.split(X)):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    scores_manual.append(acc)
    print(f'Fold {fold+1}: {acc:.4f}')

print(f'{np.mean(scores_manual):4f}')


clf2 = DecisionTreeClassifier(random_state=42)
scores_auto = cross_val_score(clf2, X, y, cv=KFold(n_splits=5, shuffle=True, random_state=42))
print(f'平均准确率: {scores_auto.mean():.4f}')