'''
不使用 `train_test_split`，用 NumPy 手动实现数据的 80/20 划分：

1. 加载 Iris 数据集
2. 使用 `np.random.seed(42)` 固定随机种子
3. 生成随机打乱的索引
4. 按 80% / 20% 划分训练集和测试集
5. 打印划分后的形状
'''

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X,y = iris.data, iris.target

idx = np.arange(len(X))

np.random.seed(42)
np.random.shuffle(idx)

X_shuffle = X[idx]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
