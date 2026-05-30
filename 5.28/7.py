import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

df['sepal_ratio'] = df['sepal length (cm)'] / df['sepal width (cm)']
df['petal_ratio'] = df['petal length (cm)'] / df['petal width (cm)']

X_original = df[iris.feature_names].values
scores_orig = cross_val_score(DecisionTreeClassifier(random_state=42), X_original, y, cv=5)
print(f"原始 4 特征 - 平均准确率: {scores_orig.mean():.4f}")

X_new = df.values
scores_new = cross_val_score(DecisionTreeClassifier(random_state=42), X_new, y, cv=5)
print(f"4 + 2 新特征 - 平均准确率: {scores_new.mean():.4f}")

if scores_new.mean() > scores_orig.mean():
    print("新特征有帮助！")
else:
    print("新特征没有明显帮助（可能对该模型/数据集无增益）")