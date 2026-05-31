# 第3周 Day18 决策树与集成学习 测试题

> **考查范围**：决策树、随机森林、GBDT、XGBoost/LightGBM、Bagging vs Boosting  
> **题型分布**：选择题 2 道（10 分）+ 简答题 1 道（10 分）+ 代码题 7 道（80 分）  
> **建议时长**：50 分钟  
> **合格线**：60 分

---

## 一、选择题（每题 5 分，共 10 分）

### 第 1 题

以下关于 Bagging 和 Boosting 的说法，**正确**的是：

A. Bagging 中各基学习器串行训练，Boosting 中各基学习器并行训练  
B. 随机森林属于 Boosting 方法  
C. Boosting 中后续模型重点关注前序模型预测错误的样本  
D. Bagging 不能降低方差，只能降低偏差

C

### 第 2 题

决策树选择分裂特征时，CART 分类树使用的准则是：

A. 信息增益（Information Gain）  
B. 信息增益比（Gain Ratio）  
C. 基尼不纯度（Gini Impurity）  
D. 均方误差（MSE）

C

---

## 二、简答题（10 分）

### 第 3 题

请简要说明 **随机森林** 相比单棵决策树的两个核心改进点，以及它为什么能降低过拟合。（100~150 字即可）

1.样本随机，训练集有放回地抽样，生成多个子训练集
2.特征随机，每次分列式，只从随机选取的特征子集中选取最优特征，增加树之间的差异性

因为是随机选取特征最优特征，抗噪声干扰能力强，然后独立训练几棵树，然后通过投票，把结果聚合起来，能够有效降低方差

---

## 三、代码题（每题约 10~12 分，共 80 分）

> 所有代码题要求使用 Python，可使用 sklearn / xgboost / lightgbm 等常用库。  
> 数据集统一使用 sklearn 自带数据集，无需额外下载。

### 第 4 题（⭐ 基础）

使用 `sklearn.datasets.load_iris()` 加载数据，完成以下操作：

1. 划分训练集和测试集（比例 8:2，随机种子 42）
2. 训练一棵 **DecisionTreeClassifier**（设置 `max_depth=3`）
3. 打印测试集准确率

### 第 5 题（⭐ 基础）

在第 4 题基础上，改用 **RandomForestClassifier**（100 棵树，随机种子 42），打印测试集准确率，并与第 4 题对比。

### 第 6 题（⭐⭐ 进阶）

使用 `sklearn.datasets.load_wine()` 数据集：

1. 用 **GradientBoostingClassifier** 训练模型（`n_estimators=100, learning_rate=0.1, max_depth=3`）
2. 打印测试集准确率和分类报告（`classification_report`）
3. 提取特征重要性并按降序打印前 5 个特征名及其重要性

### 第 7 题（⭐⭐ 进阶）

使用 `xgboost.XGBClassifier` 对 `load_breast_cancer()` 数据集进行分类：

1. 设置参数：`n_estimators=200, max_depth=4, learning_rate=0.05, eval_metric='logloss'`
2. 划分数据（8:2，随机种子 0）
3. 训练并打印测试集准确率
4. 使用 `xgboost.plot_importance` 画出特征重要性图（前 10 个）

### 第 8 题（⭐⭐ 进阶）

使用 `lightgbm.LGBMClassifier` 对 `load_digits()` 数据集（手写数字）进行分类：

1. 设置参数：`n_estimators=300, num_leaves=31, learning_rate=0.1`
2. 划分数据（7:3，随机种子 42）
3. 打印测试集准确率
4. 打印混淆矩阵

### 第 9 题（⭐⭐⭐ 综合）

在同一份数据集（`load_wine()`）上，使用 **5 折交叉验证**对比以下 4 个模型的平均准确率：

- DecisionTreeClassifier（默认参数）
- RandomForestClassifier（n_estimators=100）
- GradientBoostingClassifier（n_estimators=100）
- XGBClassifier（n_estimators=100, eval_metric='mlogloss'）

要求：
1. 使用 `cross_val_score` 计算每个模型的 5 折平均准确率和标准差
2. 打印结果对比表
3. 说明（用注释或 print）哪个模型表现最好，为什么

### 第 10 题（⭐⭐⭐ 综合）

使用 `sklearn.model_selection.GridSearchCV` 对 RandomForestClassifier 进行超参数调优：

- 数据集：`load_breast_cancer()`
- 搜索参数网格：
  - `n_estimators`: [50, 100, 200]
  - `max_depth`: [3, 5, 7, None]
  - `min_samples_split`: [2, 5, 10]
- 5 折交叉验证

要求：
1. 打印最优参数组合
2. 打印最优交叉验证得分
3. 用最优模型在测试集上评估并打印准确率
4. 对比调参前后的性能差异（默认参数 vs 最优参数）
