import matplotlib.pyplot as plt


'''
题目 3：温度变化子图（进阶）

已知：

days = [1,2,3,4,5,6,7]

high = [30,32,31,29,28,27,26]
low  = [22,21,23,24,22,20,19]

要求：

创建 两个子图：

上面的图：
绘制最高温度折线图
标题 "Highest Temperature"
下面的图：
绘制最低温度折线图
标题 "Lowest Temperature"

总要求：

使用 subplot
两个图共享 x 轴
添加网格线
使用 tight_layout()
'''

days = [1,2,3,4,5,6,7]

high = [30,32,31,29,28,27,26]
low  = [22,21,23,24,22,20,19]


fig, axe = plt.subplots(2,1,sharex = True)

axe[0].plot(days, high)
axe[0].set_title("Highest Temperature")
axe[0].grid()

axe[1].plot(days,low)
axe[1].set_title('Lowest Temperature')
axe[1].grid()

plt.tight_layout()
plt.show()