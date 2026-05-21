## 条件概率
条件概率是指某个条件下，一个事件发生的概率。
我们用公式 ```P(a|b) = P(a∩b) / P(b) ``` 来计算。

例如：小明抛硬币
```python
P_a = 0.5       # 第一次抛硬币是正面
P_b = 0.5       # 第二次抛硬币是正面
P_a_and_b = P_a * P_b       #  两次抛硬币都是正面的概率
P_b_given_b = P_a_and_b / P_a       # 在第一次抛硬币是正面的条件下，第二次抛硬币是正面的概率


```


## 贝叶斯公式
贝叶斯概率公式用来计算某个时间在新的条件之下发生的后验概率。
$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$

以疾病监测为例子：
加入某病患病率为1%，
有病时，检测阳性率为99%，
没病时，误报阳性率为5%
如果设定 A=患病，B=检测阳性
那么：
P(A) = 0.01      可以被称作先验概率，也就是原始概率，和观察到新条件后的概率相对
P(B|A) = 0.99
P(B|¬A) = 0.05

P(B)=P(B∣A)P(A)+P(B∣¬A)P(¬A)
    = 0.99×0.01 + 0.05×0.99
    = 0.0099 + 0.0495
    = 0.0594

P(A∣B)  = (0.99 × 0.01) / 0.0594     后验概率，也就是观察到了条件B之后更新的概率
        ≈ 0.1667


在python的实际运用中，贝叶斯算法一般能够通过新的条件来动态更新原来的判断，得到一个更新后的概率，
这样算是把一种经验推断用数学的方式表达出来。

```python
model = MultinomialNB()
```
python可以通过sklearn库直接创建一个多项式朴素贝叶斯模型。

朴素贝叶斯和贝叶斯的区别是，朴素贝叶斯强调所有特征相互独立，这在多文本处理任务中比较有用


## 常见分布
--------离散分布---------------------
1. 伯努利分布
1或0
$$
P(X=1)=p
$$
$$
P(X=0)=1-p
$$
比如一个硬币抛正面是1，抛反面是0
```python
np.random.binomial(1, 0.5, 10)      # 正面概率是0.5，抛10次硬币
```



2. 二项分布
进行很多次伯努利分布
$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$
抛很多次硬币，正面向上概率
```python
np.random.binomial(10, 0.5, 5)      # 一组抛10次硬币，生成5组
```

3. 泊松分布
单位时间内发生多少次事件
$$
P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}
$$
一段时间内来多少辆公交车

```python
np.random.poisson(3, 10)        # 平均每小时3辆公交车，生成10小时
array([2,4,1,3,5,2,3,4,2,1])
```


--------连续分布---------------------

4. 正态分布
中间最多，两边最少
$$
f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
成绩

```python
np.random.normal(0, 1, 10)
```

5. 均匀分布
每个结果概率都一样
$$
f(x)=\frac{1}{b-a}, \quad a \le x \le b
$$
扔骰子

```python
np.random.uniform(0, 1, 10)
```

6. 指数分布
一般研究等待时间
$$
f(x)=\lambda e^{-\lambda x}, \quad x \ge 0
$$

```python
np.random.exponential(1, 10)
```

7. 多项分布
统计多个类别出现次数，在朴素贝叶斯里常见
$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$


8. 高斯分布
近似正态分布

## 期望

长期平均结果，概率分布的中心
$$
E(X)=\sum xP(x)
$$

```python
values = [100, -50]
probs = [0.5, 0.5]

expectation = 0

for v, p in zip(values, probs):
    expectation += v * p

print(expectation)
```
```python
# 用numpy库
import numpy as np

values = np.array([100, -50])
probs = np.array([0.5, 0.5])

expectation = np.sum(values * probs)

print(expectation)
```

## 方差
方差一般表示这个数离平均值有多远，数据的波动性，方差越大越不稳定
用平方的原因是为了避免正负抵消

$$
Var(X)=E[(X-\mu)^2]
$$