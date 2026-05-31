# 第3周 Day18 决策树与集成学习 测试题 — 答案

---

## 一、选择题

### 第 1 题

**答案：C**

解析：
- A 错误：Bagging 各基学习器**并行**训练，Boosting 各基学习器**串行**训练
- B 错误：随机森林属于 **Bagging** 方法
- C 正确：Boosting 通过加大前序模型误判样本的权重来训练后续模型
- D 错误：Bagging 通过多个模型平均/投票来**降低方差**

### 第 2 题

**答案：C**

解析：
- ID3 使用信息增益（A）
- C4.5 使用信息增益比（B）
- CART 分类树使用**基尼不纯度**（C）
- CART 回归树使用均方误差（D）

---

## 二、简答题

### 第 3 题

**参考答案：**

随机森林的两个核心改进：

1. **样本随机**（Bagging）：对训练集进行有放回抽样，生成多个不同的子训练集，每棵树看到不同的数据。
2. **特征随机**：每次分裂时只从随机选取的特征子集中选择最优特征，增加了树之间的差异性。

降低过拟合的原因：单棵决策树容易过拟合（高方差），通过训练多棵差异化的树并投票/平均，可以有效**降低方差**，类似于多次测量取平均减少误差。

---

## 三、代码题

### 第 4 题

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 加载数据
X, y = load_iris(return_X_y=True)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练决策树
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)

# 评估
y_pred = dt.predict(X_test)
print(f"决策树测试集准确率: {accuracy_score(y_test, y_pred):.4f}")
```

预期输出：准确率约 0.9667

---

### 第 5 题

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 决策树
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test))

# 随机森林
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf.predict(X_test))

print(f"决策树准确率: {dt_acc:.4f}")
print(f"随机森林准确率: {rf_acc:.4f}")
print(f"随机森林相比决策树提升: {rf_acc - dt_acc:.4f}")
```

预期：随机森林准确率 ≥ 决策树（通常为 1.0 或接近）

---

### 第 6 题

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# 加载数据
data = load_wine()
X, y = data.data, data.target
feature_names = data.feature_names

# 划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练 GBDT
gbdt = GradientBoostingClassifier(
    n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42
)
gbdt.fit(X_train, y_train)

# 评估
y_pred = gbdt.predict(X_test)
print(f"GBDT 测试集准确率: {accuracy_score(y_test, y_pred):.4f}")
print("\n分类报告:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 特征重要性 Top 5
importances = gbdt.feature_importances_
indices = np.argsort(importances)[::-1][:5]
print("特征重要性 Top 5:")
for i, idx in enumerate(indices, 1):
    print(f"  {i}. {feature_names[idx]}: {importances[idx]:.4f}")
```

---

### 第 7 题

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier, plot_importance
import matplotlib.pyplot as plt

# 加载数据
X, y = load_breast_cancer(return_X_y=True)

# 划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# XGBoost 训练
xgb = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    eval_metric='logloss',
    random_state=0
)
xgb.fit(X_train, y_train)

# 评估
y_pred = xgb.predict(X_test)
print(f"XGBoost 测试集准确率: {accuracy_score(y_test, y_pred):.4f}")

# 特征重要性图（前 10）
fig, ax = plt.subplots(figsize=(10, 6))
plot_importance(xgb, max_num_features=10, ax=ax)
plt.title("XGBoost Feature Importance (Top 10)")
plt.tight_layout()
plt.savefig("xgb_feature_importance.png", dpi=100)
plt.show()
```

---

### 第 8 题

```python
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from lightgbm import LGBMClassifier
import numpy as np

# 加载数据
X, y = load_digits(return_X_y=True)

# 划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# LightGBM 训练
lgbm = LGBMClassifier(
    n_estimators=300,
    num_leaves=31,
    learning_rate=0.1,
    random_state=42,
    verbose=-1
)
lgbm.fit(X_train, y_train)

# 评估
y_pred = lgbm.predict(X_test)
print(f"LightGBM 测试集准确率: {accuracy_score(y_test, y_pred):.4f}")

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("\n混淆矩阵:")
print(cm)
```

---

### 第 9 题

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
import numpy as np

# 加载数据
X, y = load_wine(return_X_y=True)

# 定义模型
models = {
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "GBDT": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(
        n_estimators=100, eval_metric='mlogloss', random_state=42, verbosity=0
    ),
}

# 5 折交叉验证对比
print(f"{'模型':<15} {'平均准确率':<12} {'标准差':<10}")
print("-" * 37)

best_model = None
best_score = 0

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    mean_score = scores.mean()
    std_score = scores.std()
    print(f"{name:<15} {mean_score:.4f}       {std_score:.4f}")
    
    if mean_score > best_score:
        best_score = mean_score
        best_model = name

print(f"\n最优模型: {best_model}（平均准确率 {best_score:.4f}）")
print("原因: 集成方法（尤其是 Boosting 类）通过多轮迭代修正残差，")
print("在中小数据集上通常能取得比单棵树更好的泛化能力。")
```

---

### 第 10 题

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 加载数据
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === 默认参数基线 ===
rf_default = RandomForestClassifier(random_state=42)
rf_default.fit(X_train, y_train)
default_acc = accuracy_score(y_test, rf_default.predict(X_test))
print(f"默认参数测试集准确率: {default_acc:.4f}")

# === GridSearchCV 调参 ===
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)
grid_search.fit(X_train, y_train)

# 输出最优结果
print(f"\n最优参数组合: {grid_search.best_params_}")
print(f"最优交叉验证得分: {grid_search.best_score_:.4f}")

# 用最优模型在测试集上评估
best_acc = accuracy_score(y_test, grid_search.best_estimator_.predict(X_test))
print(f"最优模型测试集准确率: {best_acc:.4f}")

# 对比
print(f"\n性能对比:")
print(f"  默认参数: {default_acc:.4f}")
print(f"  调参后:   {best_acc:.4f}")
print(f"  提升:     {best_acc - default_acc:+.4f}")
```

---

## 评分标准

| 题号 | 分值 | 得分要点 |
|------|------|----------|
| 1 | 5 分 | 选对 C |
| 2 | 5 分 | 选对 C |
| 3 | 10 分 | 说出样本随机+特征随机（各 3 分），解释降低方差（4 分） |
| 4 | 10 分 | 代码能跑通（6 分）+ 正确输出准确率（4 分） |
| 5 | 10 分 | 与第 4 题对比（4 分）+ 代码正确（6 分） |
| 6 | 12 分 | GBDT 训练正确（4 分）+ 分类报告（4 分）+ 特征重要性（4 分） |
| 7 | 12 分 | XGBoost 训练正确（4 分）+ 准确率（4 分）+ 重要性图（4 分） |
| 8 | 12 分 | LightGBM 训练正确（4 分）+ 准确率（4 分）+ 混淆矩阵（4 分） |
| 9 | 12 分 | 4 模型交叉验证（8 分）+ 对比分析（4 分） |
| 10 | 12 分 | GridSearchCV 正确（6 分）+ 打印最优参数和得分（3 分）+ 对比分析（3 分） |

**总分 100 分，合格 60 分，良好 75 分，优秀 90 分。**
