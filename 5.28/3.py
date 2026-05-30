import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


iris = load_iris()

X,y = iris.data, iris.target

# wrong
scaler_wrong = StandardScaler()
X_wrong = scaler_wrong.fit_transform(X) 
X_train_w, X_test_w, _, _ = train_test_split(
    X_wrong, y,
    test_size=0.2,
    random_state=0)
print("wrong: ", X_test_w.mean(axis=0))

# correct
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,
    random_state=0)
scaler_right = StandardScaler()
X_train_scaled = scaler_right.fit_transform(X_train)  
X_test_scaled = scaler_right.transform(X_test)         
print("correct: ", X_test_scaled.mean(axis=0))