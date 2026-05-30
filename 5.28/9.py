from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf',LogisticRegression(max_iter=200))
])

pipe.fit(X_train,y_train)

y_pred = pipe.predict(X_test)
print(f'{accuracy_score(y_test,y_pred):4f}')

scores = cross_val_score(pipe, X, y, cv=5)
print(scores.mean())
