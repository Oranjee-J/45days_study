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

## 分支管理模式

### 1. 主干开发模式
在此模式中，分支存在时间段，合并频率高。
用户先把远程的main同步到本地，
然后新建分支，
在分支里开发，
然后上传到远程分支，等待管理员审核，
审核通过后合并到主分支。

多人同时开发的话可能存在冲突，主干开发模式能够尽早避免冲突，因为分支的生命周期短，同步main更加频繁，避免分支落后过多。


## 2. GitFlow模式

此模式禁止用户直接修改main的内容，只能通过合并分支来修改
GitFlow模式把不同版本的产品进行了很好的隔离，支持并行开发，避免频繁对main修改导致的发布时可能产生的冲突。
但是这个模式要求对develop分支进行频繁的更新，并且增加了分支管理的复杂程度，如果一个分支的生命周期过长，合并所消耗的时间也会变得特别多。

GitFlow模式一般有五种类型的分支：main，develop，feature，release，hotfix

- main：稳定和已发布的版本，禁止直接的修改，用来存储正式发布的产品，只能与release分支进行合并
- develop：一般代表开发中的最新集成版本，可以不是完整的产品，但是里面的功能模块必须是完整的。develop分支禁止直接修改
- feature：此分支一般用来开发功能，开发完成后合并到develop，删除此feature分支，新建feature分支继续开发
- release：一般代表待发行版本，这个分支里的产品应该是等待上线的测试和修复阶段，如果测试完成就合并到main和develop分支（打上版本标签），release禁止直接修改
- hotfix：一般从develop创建，用于进行紧急更新，修复完成后合并到main和develop分支，并打上版本标签


## 3. Github Flow模式

Github FLow可以看作是简化版的GitFlow模式。
用户先从main创建一个用于开发功能的分支，然后把分支上传到远程
然后发送 pull request，审核通过后同步到main分支

这个模式本质上也是主干开发思想的一种实践方式，但相比更激进的主干开发，GitHub Flow 更强调 pull request 和代码审核流程，协作方式也相对更温和
而此模式使得并行开发更加便捷，不容易产生设计上的冲突。

## 4. Gitlab Flow模式：
因为分支太少无法区分版本，所以Gitlab Flow里存在多个分支。
但是此模式和GitFlow模式的区别在于，main不是可发布版本，main永远代表最新的集成代码，
所有人都必须频繁更新main，这保证了开发者们开发同步

一般这个模式里还有staging分支和production分支
staging分支里开发者能够测试代码
production分支存储了能够发布的稳定版本

在此模式里，代码开发到了哪一个阶段，就在哪个分支里运行
但是当项目越来越大，分支越来越多，分别不同环境里运行的代码的版本就变得更加困难，维护成本也更高

如果实际测试出现bug，回溯就会更加困难




## 具体操作实例

### 1. 首先创建一个分支
```bash

git branch 
git branch       # 查看分支
```

### 2. 切换分支

```bash
git checkout testing
```

### 3. 其次在分支里进行文件的提交


### 4. 建立本地分支和github分支的跟踪关系

把本地testing分支上传到 GitHub 的testing分支并建立跟踪关系

```bash
git push -u origin testing
```

### 5. 合并分支至main

```bash
git merge testing
```

### 6. 更新远程main
这是最后一步了，完成这些会发现github上并没有更新，因为我们还没有把本地的main更新到githubshangqu

```bash
git push origin main
```



# Git 的其他命令
### 查看提交历史
```bash
git log
```
