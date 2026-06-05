## tensor
张量是一个多维数组，可以是标量、向量、矩阵或更高维度的数据结构。
张量支持多种数据类型，如整型、浮点型、布尔型等；张量支持GPU加速和自动梯度计算。
张量可以储存在CPU或GPU中。

| 方法 | 说明 | 示例代码 |
|------|------|----------|
| `torch.tensor(data)` | 从 Python 列表或 NumPy 数组创建张量。 | `x = torch.tensor([[1, 2], [3, 4]])` |
| `torch.zeros(size)` | 创建一个全为 0 的张量。 | `x = torch.zeros((2, 3))` |
| `torch.ones(size)` | 创建一个全为 1 的张量。 | `x = torch.ones((2, 3))` |
| `torch.empty(size)` | 创建一个未初始化的张量。 | `x = torch.empty((2, 3))` |
| `torch.rand(size)` | 创建一个服从均匀分布的随机张量，值在 `[0, 1)`。 | `x = torch.rand((2, 3))` |
| `torch.randn(size)` | 创建一个服从正态分布的随机张量，均值为 0，标准差为 1。 | `x = torch.randn((2, 3))` |
| `torch.arange(start, end, step)` | 创建一个一维序列张量，类似于 Python 的 `range`。 | `x = torch.arange(0, 10, 2)` |
| `torch.linspace(start, end, steps)` | 创建一个在指定范围内等间隔的序列张量。 | `x = torch.linspace(0, 1, 5)` |
| `torch.eye(size)` | 创建一个单位矩阵（对角线为 1，其余为 0）。 | `x = torch.eye(3)` |
| `torch.from_numpy(ndarray)` | 将 NumPy 数组转换为张量。 | `x = torch.from_numpy(np.array([1, 2, 3]))` |

将numpy数组转化成张量的方法：
```python
import numpy as np
np_array = np.array([1, 2, 3])
tensor = torch.from_numpy(np_array)
print(tensor)
```

张量的属性如下：

| 属性 | 说明 | 示例|
|------|------|----------|
| .shape|获取张量的形状|tensor.shape|
|.size()|获取张量的形状|tensor.size()|
|.dtype|获取张量的数据类型|tensor.dtype|
|.dvice|查看张量所在的设备|tensor.dvice|
|.dim()|获取张量的维度数|tensor.dim()|
|.requires_grad|是否启用梯度计算|tensor.requires_grad|
|.numel()|获取张量中的元素总数|tensor.numel()|
|.is_cuda|检查张量是否在GPU上|tensor.is_cuda|
|.T||tensor.T|
|.itm()||tensor.itm()|
|.is_contiguous()||tensor.is_contiguous()|

## Autograd
autograd指自动微分，它能够自动计算任意计算图的梯度。
自动微分不是数值微分也不是符号微分，而是通过记录计算过程、反向逐步应用链式法则来精确计算导数。
tensor的requires_grad属性控制是否需要为该张量追踪梯度。
每个由运算产生的张量都会记录一个grad_fn，指向它的操作节点。这就是计算图的骨架。

在不需要计算梯度的时候，我们可以通过torch.no_grad()来跳过计算图的构建，以此节省内存和计算。
比如梯度下降的时候，不用优化器手动更新参数，这个时候就用nograd来包裹计算过程。

## Dataset
Dataset 是 PyTorch 中用于数据集抽象的类。
自定义数据集需要继承 torch.utils.data.Dataset 并重写以下两个方法：
```__len__```：返回数据集的大小。
```__getitem__```：按索引获取一个数据样本及其标签


```python
import torch
from torch.utils.data import Dataset

# 自定义数据集
class MyDataset(Dataset):
    def __init__(self, data, labels):
        # 数据初始化
        self.data = data
        self.labels = labels

    def __len__(self):
        # 返回数据集大小
        return len(self.data)

    def __getitem__(self, idx):
        # 按索引返回数据和标签
        sample = self.data[idx]
        label = self.labels[idx]
        return sample, label

# 生成示例数据
data = torch.randn(100, 5)  # 100 个样本，每个样本有 5 个特征
labels = torch.randint(0, 2, (100,))  # 100 个标签，取值为 0 或 1

# 实例化数据集
dataset = MyDataset(data, labels)

# 测试数据集
print("数据集大小:", len(dataset))
print("第 0 个样本:", dataset[0])

```


## Dataloader
DataLoader 是 PyTorch 提供的数据加载器，用于批量加载数据集。
Dataloader具有以下功能：
- 分批加载：通过设置 batch_size来决定每一批次加载多少数据
分批次的原因是？
如果有6k张图片，每张图片28*28，那么数据维度就是（6000，28，28），一次性送入模型，内存和显存的压力会很大。如果分批次，每批次就30张图片，那么数据维度就是（30，28，28），就会大大降低压力。
- 数据打乱：通过设置 shuffle=True来决定是否打乱顺序
- 多线程加速：通过设置 num_workers来决定使用多少进程访问数据。
- 迭代访问：方便地按批次访问数据。dataloader是一个可迭代对象，这样可以处理任意大小的数据集，不需要自己去管理数据的分组和顺序。



## nn.Module
torch.nn.Moduel是pytorch中所有神经网络模型的基类，它提供了神经网络的构建、参数管理和前向传播等功能，具体来说，它的功能包括：
1. 定义多层神经网络（神经网络的每个层都可以是其他Module实例
2. 前向传播：通过Module，我们可以自定义前向传播逻辑。前向传播决定输入数据如何经过各层处理并生成输出。
3. 参数管理：Module类可以自动管理网络中的所有参数
4. 模块嵌套：Module中定义的子模块可以嵌套，形成复杂的模型结构
5. 模式切换：Module提供train方法和eval方法，分别切换模型的训练和评估方法
6. 设备管理：Module提供to方法，可以将模型及其参数移动到指定的设备如GPU上。


## 优化器

- 自动化参数更新：手动计算和更新每个参数非常繁琐，优化器自动完成这一工作
- 加速收敛：使用优化算法比普通梯度下降更快找到最优解
- 避免局部最优：某些优化器具有跳出局部最优的能力

优化器的使用遵循固定模式：创建实例 → 清空梯度 → 反向传播 → 更新参数

```python

# 1. 定义一个简单的模型
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(784, 10)

    def forward(self, x):
        return self.fc(x)

model = SimpleNet()

# 2. 创建优化器实例
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. 训练循环
for epoch in range(epochs):
    # 前向传播
    outputs = model(inputs)
    loss = criterion(outputs, labels)

    # 反向传播
    optimizer.zero_grad()  # 清空梯度缓存，避免梯度累积
    loss.backward()        # 计算梯度

    # 参数更新
    optimizer.step()       # 更新参数

```

为什么总是要清空梯度？因为梯度默认累计。
优化器一定要先backward()再step()因为先有梯度，才能用梯度更新参数。