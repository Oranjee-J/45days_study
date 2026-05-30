from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

print(f"{'test size':<12}{'train':<10}{'test':<10}{'accuracy':<12}")

for size in [0.1, 0.2, 0.3, 0.5, 0.7]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=size,
        random_state=42
        )
    clf = LogisticRegression(max_iter=200)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"{size:<12}{X_train.shape[0]:<10}{X_test.shape[0]:<10}{acc:<12.4f}")