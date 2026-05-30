import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# 随机制造缺失值
np.random.seed(0)
mask = np.random.random(df.shape) < 0.1
df_missing = df.mask(mask)

#均值填充
df_mean = df_missing.fillna(df_missing.mean())
scores_mean = cross_val_score(DecisionTreeClassifier(random_state=42), df_mean.values, y, cv=5)
print(f"accuracy_mean: {scores_mean.mean():.4f}")

# 中位数填充
df_median = df_missing.fillna(df_missing.median())
scores_median = cross_val_score(DecisionTreeClassifier(random_state=42), df_median.values, y, cv=5)
print(f"accuracy_median: {scores_median.mean():.4f}")