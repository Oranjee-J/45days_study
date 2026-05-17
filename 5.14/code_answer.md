## 1. 变量与数据类型
双等号的作用是判断值是否相等，python可以跨类型比较值，所以对于int类型和float类型的数据可以直接比较，但是string字符串类型并不属于数值数据类型，所以str和int之间并没有数值关系，比较结果是False

## 2. 列表推导
range左边包含右边不包含

## 3. 字典操作

- 空字典创建使用大括号
- 遍历字典的方法：
1. 根据key： '''for k in d'''
2. 根据key和value： '''for k,v in d.items():'''
3. 更新字典： '''d.update(d_new)'''，此处 d_new 应为一个新的要合并的字典

'''top_student = max(scores, key=scores.get)'''
能够直接找出字典中最大scores的学生名字，而无需遍历
'''avg = round(sum(scores.values()) / len(scores), 2)'''
2代表保留两位小数，字典的sum可以直接把value加在一起无需遍历
'''high_scores = {k: v for k, v in scores.items() if v >= 90}'''
更加简洁



## 4. 字符串处理
字符串的s.split()默认根据空格、换行、制表符来切分字符串，切分之后得到的是一个列表。
使用.capitalize()方法能够将每个单词的首字母大写，其余字母小写
然后要将列表变回字符串，令'''result = ' '.join(列表)'''
.upper()能够将字母变成大写的。
对于字符串的任何操作都不能改变原有的字符串，只是创建了新的字符串\令变量指向新的字符串


## 5. 切片与反转
'''list = [start:end:step]'''

step<0 为倒序遍历
start/end <0 :反向索引编号， -1是倒数第一个
列表，元组，字符串均可以反向索引，也都能够切片


## 6.异常处理

.isinstance( 变量 , 类型 ) 只要有一个数据类型符合则输出True
如果有多个类型则用括号括起来，以逗号连接



## 7.集合运算

a|b             :   并集，包含所有元素去重       
a-b             :   差集，a有b没有的元素
b-a             :   差集，b有a没有的元素
a^b             :   对称差集，只属于a或只属于b的元素
a&b             :   交集，又属于a又属于b的元素
.isdisjoint()   :   是否有交集，没有的话输出True
.issubset()     :   子集
.issuperset()   :   超集


## 8.可变与不可变对象

不可变数据类型： int， float， tuple， str， bool， frozenset


## 9.默认参数陷阱
可变数据类型当参数是，让lst = None来避免参数共享（具体视情况而定）

## 10.*args和**kwargs
都能传不确定数量的参数
*args： 传入格式'''a,b,c'''， 打包成元组
**kwargs：传入格式'''name = 'Alice', age = 18, Location = 'London' '''，打包成字典

混合参数里，*args一定在**kwargs前面



## 11.闭包

nonlocal声明了counter之后，能够在inner函数里修改外部函数的变量，间接将其保存下来，这样子不会导致每次调用时，counter都重新初始化为0.
闭包三要素：
嵌套函数，引用外层变量，外层函数返回内层函数

## 12.装饰器
使用@functools.wraps()来把里面的wrapper函数伪装成func的样子，以便日志追踪

## 13.递归展平列表
extend方法：将括号里的列表和外面的合并

## 14. lambda
map 提取
filter 筛选
sorted 排序

- `map(func, iterable)` 对每个元素应用函数
- `filter(func, iterable)` 保留返回 True 的元素
- `sorted(key=...)` 自定义排序键



## 15.基础类定义

前后都带双下划线的函数能让函数像对象一样工作

## 16.继承与方法重写
子类能直接继承父类的实例方法和类属性。
对于实例对象，写super().__init__(对象)即可继承

## 17.类方法，静态方法

类属性定义在实例方法的外面，如果是计数，则在init函数中计算，如 '''Task.task_count += 1'''
类方法能够用来更改类属性，第一个参数是cls
静态方法不接受self和cls

## 18.魔术方法
魔术方法就是左右都带两个下划线的方法，
这个要死记硬背。


## 19.属性装饰器
背下来

## 20.综合实战

注意点：
1. 如何规定实例对象范围
2. 添加任务就是新建一个列表加入所有的任务名称
3. 排序需要用到lamba函数
4. total是任务多少，complete是完成任务数量，pending是未完成的数量
5. len是计算长度的魔术方法，iter是迭代的魔术方法