import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

'''
题目 2：水果销量柱状图（中等）

已知水果销量：

fruits = ["Apple", "Banana", "Orange", "Grape"]
sales = [35, 50, 40, 60]

要求：

使用柱状图 (bar)
设置标题 "Fruit Sales"
设置 y 轴标签 "Count"
给每个柱子顶部显示具体数字
调整柱子的宽度

额外挑战（可选）：

修改柱子的颜色
添加网格线
'''




sns.set_theme(style="darkgrid", palette="pastel")

fruits = ["Apple", "Banana", "Orange", "Grape"]
sales = [35, 50, 40, 60]

bars = sns.barplot(
    x=fruits, y=sales,
    width= 0.5,
    color = 'yellow'
    )

for bar in bars.patches:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,
        height,
        f'{height}',
        ha = 'center',
        va = 'bottom'
        )

plt.xlabel('Fruits')
plt.ylabel('Count')
plt.title('Fruit Sales')

plt.show()