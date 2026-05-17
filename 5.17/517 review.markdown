# Matpotlib

## 安装和使用

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

## 设置标签和标题的方法

通过以下函数即可设置x、y轴标签以及图标的标题

```python
plt.xlabel(' ')
plt.ylabel(' ')

plt.title(' ')

plt.grid(axis = 'x')        # 在x轴方向展示网格线
```



## 创建其他图的方法


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

子图可以

```python


plt.subplot(2,1,1)
plt.plot(x,y)
plt.set_title(' ')

plt.subplot(2,1,2)
plt.plot(x,y)
plt.set_title('')

```
对于plt.subplot(x,y,index)来说，x代表将行分割成x份，y代表将列分割成y份，index代表图画在第几个空里。



```python
fig, axe = plt.subplots(2,1,sharex = True)

axe[0].plot(days, high)
axe[0].set_title("Highest Temperature")
axe[0].grid()

axe[1].plot(days,low)
axe[1].set_title('Lowest Temperature')
axe[1].grid()
```



# Git

首先我们到git的官网里去下载并安装git，然后打开git bash开始配置环境。

要想从本地直接上传到github自己创建的仓库里，我们需要执行以下几个步骤：
1.建立仓库
2.配置用户名与邮箱
3.配置ssh
- 生成ssh密钥
- 将ssh密钥添加到ssh代理
- 在github添加公钥
- 使用ssh链接克隆仓库
4.上传文件

## 1.建立仓库、
在github新建仓库即可

## 2. 配置用户名与邮箱

- 打开Git Bash

```bash
git config --global user.name "github上的注册的用户名" # 例如我的用户名 "Oranjee-J"
git config --global user.email "github上的注册的邮箱" # 例如我的邮箱 "2775429497@qq.com"
git config --global --list
```

## 3. 配置ssh
- 生成ssh密钥

因为我的用户名是中文，如果用默认路径，路径里会包含乱码，导致无法生成密钥，所以先查看路径

```bash
ls /c/Users         # 查看目录
mkdir -p /c/Users/小橘/.ssh
ssh-keygen -t rsa -b 4096 -C "2775429497@qq.com" -f /c/Users/小橘/.ssh/id_rsa
```
然后一路回车，然后就能生成密钥了。

然后用以下命令来查看密钥，注意私钥不能发给别人！
```bash
cat /c/Users/小橘/.ssh/id_rsa.pub       # 公钥
cat /c/Users/小橘/.ssh/id_rsa           # 私钥
```
- 将ssh密钥添加到ssh代理
我目前没有添加，不影响使用。

- 在github添加公钥
然后把公钥全部复制下来，然后进入github，点击头像，进入设置，然后添加公钥。

- 使用ssh链接克隆仓库

先在本地新建一个github文件夹：
```bash
cd /c/Oranjee/gitproject/github 
git clone git@github.com:Oranjee-J/45days_study.git
```
这样就能克隆仓库了。

然后再进入这个本地的仓库文件夹，可以把文件上传到github里去：
```bash
git add .           # 全部上传
git add main.py     # 上传某一个
git add data/       # 上传文件夹下变化的文件

```


```bash
git commit -m "Initial commit"
git push origin main
```


# Git的分支管理

我们可以通过分支管理，来进行文件的更新。分支管理使得某一次更新在确认之后才会上传到main分支。
对于大型项目比如说一个游戏来说，游戏可以进行beta测试，当这个测试经过反复修改之后，确定可以作为正式版本的更新，再更新到mian。
可以这样理解。

## 首先创建一个分支
```bash

git branch 
git branch       # 查看分支
```


## 切换分支

```bash
 git checkout testing

```

## 其次在分支里进行文件的提交


## 建立本地分支和github分支的跟踪关系

把本地testing分支上传到 GitHub 的testing分支并建立跟踪关系

```bash
git push -u origin testing
```

## 合并分支至main

```bash
git merge testing

```