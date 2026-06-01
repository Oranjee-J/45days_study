# 分类模型四个常用评价指标

首先定义混淆矩阵：
|                | 预测为正类 | 预测为负类 |
| -------------- | ---------- | ---------- |
| 实际为正类     | TP         | FN         |
| 实际为负类     | FP         | TN         |

其中：
- TP（True Positive）：真正例
- TN（True Negative）：真负例
- FP（False Positive）：假正例
- FN（False Negative）：假负例


## 1. Accuracy（准确率）
表示预测正确的样本占总样本的比例。
\[Accuracy=\frac{TP+TN}{TP+TN+FP+FN}\]
缺点：在数据不平衡时具有误导性。例如，如果 99% 的邮件都是正常邮件，一个把所有邮件都预测为正常的"笨模型"，准确率也能高达 99%，但它一个垃圾邮件都抓不到。

## 2. Precision（精确率）
表示预测为正类的样本中，实际为正类的比例。
\[Precision=\frac{TP}{TP+FP}\]
问题：在我们预测为垃圾邮件的邮件中，有多少真的是垃圾邮件？ 高精确率意味着：模型说"这是垃圾邮件"时，可信度很高。

## 3. Recall（召回率）
表示实际为正类的样本中，被正确预测为正类的比例。
\[Recall=\frac{TP}{TP+FN}\]
问题：在所有真正的垃圾邮件中，我们找出了多少？ 高召回率意味着：模型很少漏掉真正的垃圾邮件

## 4. F1-Score
Precision 和 Recall 的调和平均数。
\[F1=\frac{2 \times Precision \times Recall}{Precision + Recall}\]
也可以直接写成：
\[F1=\frac{2TP}{2TP+FP+FN}\]
它更倾向于惩罚极端值。只有当精确率和召回率都较高时，F1 分数才会高

## 总结
| 指标 | 公式 |
|--------|--------|
| Accuracy | \(\frac{TP+TN}{TP+TN+FP+FN}\) |
| Precision | \(\frac{TP}{TP+FP}\) |
| Recall | \(\frac{TP}{TP+FN}\) |
| F1-Score | \(\frac{2PR}{P+R}\) |

其中：
\[P = Precision\]
\[R = Recall\]



## AUC
ROC曲线是一种用于表示分类模型性能的图形工具。它通过将真阳性率（True Positive Rate，TPR）和假阳性率（False Positive Rate，FPR）作为横纵坐标来描绘分类器在不同阈值下的性能。
真阳性率也指召回率。
AUC（ROC曲线下面积）是ROC曲线下的面积，用于衡量分类器性能。AUC值越接近1，表示分类器性能越好；反之，AUC值越接近0，表示分类器性能越差。在实际应用中，我们常常通过计算AUC值来评估分类器的性能。

理论上，完美的分类器的AUC值为1，而随机分类器的AUC值为0.5。这是因为完美的分类器将所有的正例和负例完全正确地分类，而随机分类器将正例和负例的分类结果随机分布在ROC曲线上。

roc_curve函数：
首先需要导入metrics库。
roc_curve函数需要输入以下参数：
y_true: 实际目标值，通常是二进制的（0或1
y_score:分类器为每个样本计算的概率或决策函数得分

fpr: 假阳性率
tpr: 真阳性率
thresholds: 计算得到的阈值

## Grid Search CV

```https://blog.csdn.net/feizuiku0116/article/details/154354658```

网格搜索是一种超参数搜索方法，它在指定的参数网格中穷举所有组合，然后通过交叉验证自动评估每组参数的性能，从而找到最优参数组合。

它的执行流程如下：

1. 设定一个参数搜索空间（网格）
2. 对每组参数组合进行 K 折交叉验证
3. 计算验证集上的平均得分
4. 选出平均得分最高的参数组合作为最优结果


```
best_score = -inf
for param_combo in parameter_grid:
    scores = []
    for train_idx, val_idx in KFold(data, k=5):
        model = Model(param_combo)
        model.fit(X[train_idx], y[train_idx])
        score = model.score(X[val_idx], y[val_idx])
        scores.append(score)
    avg_score = mean(scores)
    if avg_score > best_score:
        best_score = avg_score
        best_params = param_combo

```
