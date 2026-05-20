#  numpy库里那些和线性代数有关的函数

## 生成矩阵

1. np.array()

2. np.zeros
    np.eye
    np.ones

3. np.random.randn(shape)   标准正态分布矩阵

4. np.random.uniform(start, end, shape)     均匀分布矩阵

## 高维操作

1. a.shape 查看shape

2. a.reshape 重新改变形状，逻辑顺序不变

3. a.T      矩阵倒置
    np.transpose(a,(1,0,2))     高维矩阵倒置，注意后面括号里写的是轴编号！1，0，2代表从0，1，2变过来，是第一维和第二维交换顺序！编号[i,j,k]的元素会变成编号[j,i,k]


4. a.swapaxes(0,1)

5. np.squeeze(a)    删除长度为1的维度

6. np.expand_dims(a,axis=0)     增加维度



## 矩阵运算 **

1. Q @ W        矩阵乘法
    np.matmul(A,B)

2. np.dot(a,b)      点积  

3. np.linalg.norm(a)        向量长度（范数）

4. np.sum(a)
    np.sum(a,axis=1)    按行求和

5. np.mean(a)       均值

6. np.max(a)        最大值

7. np.linalg.inv(A)     求逆矩阵
深度学习中很少直接计算逆矩阵的原因
- 计算复杂度高：$O(n^3)$，对大矩阵不现实
- 数值不稳定：接近奇异的矩阵求逆会导致大误差
- 实际可以用梯度下降等迭代方法替代求逆操作

8. np.linalg.det(A)     求行列式

9. eigenvalues, eigenvectors = np.linalg.eig(A)     求特征值和特征向量

10. U,S,Vt = np.linalg.svd(A)       SVD

11. np.linalg.matrix_rank(A)        矩阵秩
    矩阵秩实际上是求有多少行是独立信息， 也就是不能被其他行表示

12. Ax = b, np.linalg.solve(A,b)    求解线性方程组

13. np.cov(X.T)     协方差矩阵

14. np.exp(x)       指数

13. np.sqrt(x)      平方根

14. np.argmax(x)    最大值的下标


# SVD分解
简单来说，SVD是将一个任意矩阵分解为三个矩阵。所以如果我们有一个矩阵A，那么它的SVD可以表示为：
```A = USV^T ```
U和V都是特征方向
S是特征值对角阵（只有对角线上有A^TA的特征值的平方根，其余元素为0，这些特征值就是奇异值，奇异值永远非负）

奇异值表示信息强度。SVD压缩用于那些低秩的矩阵，用来压缩信息，来去除那些冗余信息

把复杂变换分解成旋转，拉伸，旋转的步骤




# PCA降维

1. 计算均值，数据中心化（原始值减均值）

2. 计算协方差矩阵

3. 特征值分解

4. 排序，选择主成分

5. 投影数据，得到降维后的结果


```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 加载数据
iris = load_iris()
X = iris.data  # (150, 4)

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA 降到 2 维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("降维后形状：", X_pca.shape)  # (150, 2)
print("各主成分方差解释比例：", pca.explained_variance_ratio_)
print("前两个主成分累计解释方差：", sum(pca.explained_variance_ratio_))
```


```python
import numpy as np

# 1. 中心化
X_centered = X - np.mean(X, axis=0)

# 2. 协方差矩阵
cov_matrix = np.cov(X_centered.T)

# 3. 特征值分解
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# 4. 取最大两个特征向量
idx = np.argsort(eigenvalues)[::-1]

top2 = eigenvectors[:, idx[:2]]

# 5. 投影
X_pca = X_centered @ top2

```

# 每周总结
这周最大的短板是装饰器的代码实现，属性装饰器和魔术方法都不太熟练（不熟悉形式）
不会熟练应用装饰器、一行代码和匿名函数
pca没有记住步骤是什么（自己不会解释），svd的代码不会写，numpy的矩阵运算练习的不太多，对于numpy库里线性代数相关的函数记忆不全面

