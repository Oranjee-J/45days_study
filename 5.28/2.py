'''

1. 加载 Iris 数据集
2. 选取第 1 个特征（花萼长度）
3. 分别用 `StandardScaler`（标准化）和 `MinMaxScaler`（归一化）处理
4. 打印处理前、标准化后、归一化后的均值和标准差
5. 用 `print` 对比三者的 min 和 max

'''

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

iris = load_iris()

X = iris.data
scaler_1 = StandardScaler()
scaler_2 = MinMaxScaler()

print(f'X.means: {X.mean():.4f}')
print(f'X.std: {X.std():.4f}')

print(X.min())
print(X.max())

scaler_1.fit_transform(X)
X_scaler_1 = scaler_1.transform(X)
print(f'X_standard scaler mean: {X_scaler_1.mean():.4f}')
print(f'X_std: {X_scaler_1.std():.4f}')
print(X_scaler_1.min())
print(X_scaler_1.max())

scaler_2.fit_transform(X)
X_scaler_2 = scaler_2.transform(X)
print(f'X_minmax scaler mean: {X_scaler_2.mean():.4f}')
print(f'X_std: {X_scaler_2.std():.4f}')
print(X_scaler_2.min())
print(X_scaler_2.max())