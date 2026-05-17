## Matpotlib

# 安装和使用

首先进入虚拟环境，在终端输入```pip install matplotlib```即可

```python
import matplotlib
print(matplotlib.__version__)
```
能成功打印matplotlib的版本就是安装完成了。

这次学习的绘图主要用的是matplotlib里的pyplot库。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi,0.1)
y = sin(x)
z = cos(x)

plt.plot(x,y.x.z)
plt.show()
```
我们可以在设定好x，y之后通过.plot()和.show()函数来生成一个图，并且打印它。

一张图里可以输入两组x，y。输入后图上会显示两条线。

plot里有很多参数可以自由设置。

marker              自定义标记
linestyle(ls)       定义线的类型
color(c)            定义线的颜色
linewidth           定义线的宽度

# 设置标签和标题的方法

通过以下函数即可设置x、y轴标签以及图标的标题

```python
plt.xlabel(' ')
plt.ylabel(' ')

plt.title(' ')

plt.grid(axis = 'x')        # 在x轴方向展示网格线
```



# 创建其他图的方法


### 创建柱形图
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x,y)
plt.show()
```
barh() 创建垂直的柱形图


如果想要显示每一个柱子的数值可以这样做：

```python
x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])


bars = plt.bar(x,y)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,
        height,
        f'{height}',
        ha = 'center',
        va = 'bottom'
        )    

plt.show()
```
如果通过seaborn创建了柱形图，需要通过```for bar in bars.patches```才能遍历了。




### 子图的创建
