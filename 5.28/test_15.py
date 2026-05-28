from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
X, y = iris.data, iris.target

cls = DecisionTreeClassifier()

scores = cross_val_score(cls, X, y, cv = 5, scoring = 'accuracy')
print(scores)
print(f'每折的准确率：{scores.mean():.4f}')
print(f'标准差： {scores.std():.4f}')