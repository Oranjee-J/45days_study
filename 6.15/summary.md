# 深度学习选择题（20题）

## 1. 神经网络中的激活函数主要作用是什么？

A. 增加模型参数数量  
B. 引入非线性能力  
C. 降低训练数据量  
D. 提高数据维度


**B**
---

## 2. 下列哪个激活函数最容易出现梯度消失问题？

A. ReLU  
B. Leaky ReLU  
C. Sigmoid  
D. GELU

**C**

---

## 3. 在神经网络训练中，反向传播算法的主要作用是？

A. 计算模型预测值  
B. 更新训练数据  
C. 计算损失函数  
D. 计算参数梯度

**D**

---

## 4. 梯度下降法的核心思想是？

A. 沿梯度方向更新参数  
B. 沿梯度反方向更新参数  
C. 随机更新参数  
D. 固定参数不变

**B**

---

## 5. 下列哪种优化器引入了动量（Momentum）机制？

A. SGD  
B. Momentum SGD  
C. Adagrad  
D. RMSprop

**B**

---

## 6. Adam优化器结合了哪些优化思想？

A. Momentum 和 RMSprop  
B. SGD 和 BatchNorm  
C. Dropout 和 Momentum  
D. ReLU 和 SGD

**A**

---

## 7. Dropout层的主要作用是？

A. 提高训练速度  
B. 减少参数数量  
C. 防止过拟合  
D. 增加神经元数量

**C**

---

## 8. Batch Normalization通常放置在什么位置？

A. 激活函数之后  
B. 激活函数之前  
C. 输出层之后  
D. 损失函数之后

**B**

---

## 9. 对于多分类问题，输出层通常使用哪种激活函数？

A. ReLU  
B. Sigmoid  
C. Softmax  
D. Tanh

**C**

---

## 10. 交叉熵损失函数最常用于哪类任务？

A. 回归任务  
B. 聚类任务  
C. 分类任务  
D. 降维任务

**C**

---

## 11. 卷积神经网络（CNN）中的卷积层主要用于？

A. 特征提取  
B. 数据增强  
C. 参数初始化  
D. 损失计算

**A**

---

## 12. CNN中的池化层（Pooling Layer）主要作用是？

A. 增加特征图尺寸  
B. 减少特征图尺寸并保留重要信息  
C. 增加模型参数数量  
D. 提高输入分辨率

**B**

---

## 13. 在CNN中，共享权重（Weight Sharing）的优点是？

A. 提高参数数量  
B. 减少参数数量  
C. 增加训练时间  
D. 防止梯度下降

**B**

---

## 14. RNN适合处理哪类数据？

A. 表格数据  
B. 图像数据  
C. 序列数据  
D. 聚类数据

**C**

---

## 15. 普通RNN在长序列训练中容易出现什么问题？

A. 参数爆炸  
B. 维度灾难  
C. 梯度消失或梯度爆炸  
D. 数据泄漏

**C**

---

## 16. LSTM相比普通RNN增加了什么机制？

A. 卷积核  
B. 注意力机制  
C. 门控机制  
D. BatchNorm

**C**

---

## 17. GRU与LSTM相比最大的特点是？

A. 参数更少，结构更简单  
B. 没有循环结构  
C. 不支持长序列  
D. 不需要反向传播

**A**

---

## 18. Transformer模型中最核心的机制是什么？

A. 卷积机制  
B. 池化机制  
C. 自注意力机制（Self-Attention）  
D. 门控机制

**C**

---

## 19. Transformer相比RNN的主要优势之一是？

A. 无法并行计算  
B. 可以并行处理序列  
C. 参数更少  
D. 不需要训练

**B**

---

## 20. 在Self-Attention中，每个词向量通常会映射成哪三个向量？

A. Input、Output、Loss  
B. Mean、Variance、Bias  
C. Query、Key、Value  
D. Weight、Bias、Gradient

**C**

---