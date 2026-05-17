'''
题目 1：学生成绩折线图（基础）

有 5 次考试成绩：

scores = [72, 75, 78, 83, 88]

要求：

使用 matplotlib 绘制折线图
x 轴显示“第1次”到“第5次”
添加标题 "Score Trend"
给 x 轴、y 轴添加标签
给每个点显示圆点 marker

效果类似：

折线
每个数据点有圆圈
能看出成绩上升趋势
'''





import matplotlib
import matplotlib.pyplot as plt
import numpy as np

number = ['第一次','第二次','第三次','第四次','第五次']
score = [72,75,78,83,88]
plt.plot(number,score,marker = 'o')
plt.title('Score Trend')
plt.xlabel('test numeber')
plt.ylabel('score')
plt.show()

