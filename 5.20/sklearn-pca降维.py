import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

print('shape of origin datasets:',X.shape)

scaler = StandardScaler()   # 标准化
X_scaled = scaler.fit_transform(X)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print('shape after pca:', X_pca.shape)

print('主成分贡献率：')
print(pca.explained_variance_ratio_)
print('累计贡献率')
print(pca.explained_variance_ratio_.sum())

plt.figure(figsize=(8,6))

for label in range(3):
    plt.scatter(
        X_pca[y == label, 0],
        X_pca[y == label, 1],
        label=iris.target_names[label]
    )

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of Iris Dataset")
plt.legend()

plt.show()