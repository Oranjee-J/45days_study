from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from lightgbm import LGBMClassifier
import numpy as np

X, y = load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

lgbm = LGBMClassifier(
    n_estimators=300,
    num_leaves=31,
    learning_rate=0.1,
    random_state=42,
    verbose=-1
)
lgbm.fit(X_train, y_train)

y_pred = lgbm.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(acc)

cm = confusion_matrix(y_test, y_pred)
print("cofustion matrix:\n")
print(cm)