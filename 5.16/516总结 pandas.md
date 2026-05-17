## 安装pandas
因为已经用anaconda建好了虚拟环境，所以在虚拟环境里安装就好了，不要在本地base环境里安装，不然容易导致环境的混乱和版本混淆。先conda activate激活虚拟环境，然后用pip install或者conda install就可以了。

```python
import pandas as pd
print(pd.__version__)
```

能正常查看pandas环境就是装好了。


## 创建数据结构
pandas有两个核心数据结构，分别是Series和DataFrame；
Series 类似一个一维数组，可以储存任何数据类型，并通过标签来访问元素。
```python
a = pd.Series(['Bob',2,18,60]，index = ['Name','Grade','Age','Score'], name = 'Bob')
```
index默认是0，1，2，3；不过我们可以在创建的时候手动设置index。name就是对象的名称。
如果设置了两个Series，然后把这两个Series合并，name就会自动变成列名。

DataFrame可以通过二维数组来创建，也可以通过字典来创建。

```python
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
a = pd.DataFrame(data,column = ['Site', 'Age'])
a['Site'] = a['Site'].astype(str)       # 这样设置每一列的数据类型
a['Age'] = a['Age'] .astype(int)
```

```python
student = pd.DataFrame({
    'Number' : [1,2,3,4,5]
    'Name' : ['a','b','c','d','e']
    'age' : [14,15,13,14,15]
})
```

如果第一个Series的key只有'name','age'，第二个Series的key只有'number','age'，这两个Series相加，并不会报错，pandas会自动把这个Series没有的key列用NaN值填充，这也是我们数据清洗有时候需要去除的地方。虽然处理NaN可能造成信息的损失和误差，但是这会使某些数学运算或者机器模型产生错误。

我们可以把numpy和pandas结合起来构建数据集，这样看起来更加清晰一点。
并且通过numpy构建二维数组，可以通过numpy库来调用库里的函数，来进行矩阵运算。
譬如二维数组 ```a = [[1,2],[3,4]]```, a*2 的结果是[[1,2],[3,4],[1,2],[3,4]]。
但是通过numpy创建的二维数组a就可以直接进行矩阵的运算（list不能被看作是矩阵），得到的结果是[[2,4],[6,8]]。

```python
data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])

dataset = pd.DataFrame(data,columns = ['Site','Age'])
```

## 读取数据
如果想从一个DataFrame中读取数据，可以通过loc索引来读取。

```python
data.loc['Site']
```


方法名称	        功能描述
-----------------------------------------------------------------------------------
head(n)	            返回 DataFrame 的前 n 行数据（默认前 5 行）
tail(n)	            返回 DataFrame 的后 n 行数据（默认后 5 行）
info()	            显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
describe()	        返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等
shape	            返回 DataFrame 的行数和列数（行数, 列数）
columns	            返回 DataFrame 的所有列名
index	            返回 DataFrame 的行索引
dtypes	            返回每一列的数值数据类型
sort_values(by)	    按照指定列排序
sort_index()	    按行索引排序
dropna()	        删除含有缺失值（NaN）的行或列
fillna(value)	    用指定的值填充缺失值
isnull()	        判断缺失值，返回一个布尔值 DataFrame
notnull()	        判断非缺失值，返回一个布尔值 DataFrame
loc[]	            按标签索引选择数据
iloc[]	            按位置索引选择数据
at[]	            访问 DataFrame 中单个元素（比 loc[] 更高效）
iat[]	            访问 DataFrame 中单个元素（比 iloc[] 更高效）
apply(func)	        对 DataFrame 或 Series 应用一个函数
applymap(func)	    对 DataFrame 的每个元素应用函数（仅对 DataFrame）
groupby(by)	        分组操作，用于按某一列分组进行汇总统计
pivot_table()	    创建透视表
merge()	            合并多个 DataFrame（类似 SQL 的 JOIN 操作）
concat()	        按行或按列连接多个 DataFrame
to_csv()	        将 DataFrame 导出为 CSV 文件
to_excel()	        将 DataFrame 导出为 Excel 文件
to_json()	        将 DataFrame 导出为 JSON 格式
to_sql()	        将 DataFrame 导出为 SQL 数据库
query()	            使用 SQL 风格的语法查询 DataFrame
duplicated()	    返回布尔值 DataFrame，指示每行是否是重复的
drop_duplicates()	删除重复的行
set_index()	        设置 DataFrame 的索引
reset_index()	    重置 DataFrame 的索引
transpose()	        转置 DataFrame（行列交换）



```python
import pandas as pd

# 创建 DataFrame
dt = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
data = pd.DataFrame(data)


print(data.head(2))                                             # 查看前两行数据
print(ddata.info())                                             # 查看 DataFrame 的基本信息

print(data.describe())                                          # 获取描述统计信息

data_sorted = data.sort_values(by='Age', ascending=False)       # 按年龄排序
print(data_sorted)

print(data[['Name', 'Age']])                                    # 选择指定列

print(data.iloc[1:3])  # 选择第二到第三行（按位置）               # 按索引选择行

print(data.loc[1:2])  # 选择第二到第三行（按标签）                # 按标签选择行

print(data.groupby('City')['Age'].mean())                       # 计算分组统计（按城市分组，计算平均年龄）

data['Age'] = data['Age'].fillna(30)                            # 处理缺失值（填充缺失值）

data.to_csv('output.csv', index=False)                          # 导出为 CSV 文件
```



```python
# DataFrame 的属性和方法
print(df.shape)     # 形状
print(df.columns)   # 列名
print(df.index)     # 索引
print(df.head())    # 前几行数据，默认是前 5 行
print(df.tail())    # 后几行数据，默认是后 5 行
print(df.info())    # 数据信息
print(df.describe())# 描述统计信息
print(df.mean())    # 求平均值
print(df.sum())     # 求和
```


我们可以直接通过data['column_name]=[]来对列进行赋值
通过data['new_column']=[]可以添加新的列

如果想要对行进行更改，可以这样写代码：
data['index'] = []

如果想要添加行，建议使用concat，append在pandas将是一个被弃用的方法
```python
data = data.append(new_row,ignore_index = True)
data.concat([df, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
```

合并DataFrame的方法：

concat --- 纵向合并
merge ---横向合并



## csv数据读取
```python

# 最基本的读取
df = pd.read_csv("data.csv")

# 指定编码（处理中文文件常用）
df_utf8 = pd.read_csv("data.csv", encoding="utf-8")
df_gbk = pd.read_csv("data.csv", encoding="gbk")

# 跳过行（跳过表头后的行或注释行）
df = pd.read_csv("data.csv", skiprows=3)  # 跳过前3行
df = pd.read_csv("data.csv", skiprows=[2, 4])  # 跳过第2、4行

# 使用表头行（默认第一行）
df = pd.read_csv("data.csv", header=0)  # 第0行作为表头
df = pd.read_csv("data.csv", header=None)  # 不使用表头，自动生成 0,1,2...

# 指定列名
df = pd.read_csv("data.csv", names=["ID", "姓名", "年龄", "城市"])

# 指定索引列
df = pd.read_csv("data.csv", index_col=0)  # 第0列作为索引
df = pd.read_csv("data.csv", index_col=["姓名"])  # 多列作为复合索引
```


## 数据清洗和预处理

1. 缺失值处理：识别并填补缺失值，或删除含缺失值的行/列。
2. 重复数据处理：检查并删除重复数据，确保每条数据唯一。
3. 异常值处理：识别并处理异常值，如极端值、错误值。
4. 数据格式转换：转换数据类型或进行单位转换，如日期格式转换。
5. 标准化与归一化：对数值型数据进行标准化（如 Z-score）或归一化（如 Min-Max）。
6. 类别数据编码：将类别变量转换为数值形式，常见方法包括 One-Hot 编码和标签编码。
7. 文本处理：对文本数据进行清洗，如去除停用词、词干化、分词等。
8. 数据抽样：从数据集中抽取样本，或通过过采样/欠采样处理类别不平衡。
9. 特征工程：创建新特征、删除不相关特征、选择重要特征等。


- 缺失值处理

只要包含NaN值就去除整行
```python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```
dropna默认返回一个新的DataFrame（inplace = False）

一般对于一个比较小的数据集进行处理，如果直接去掉整行可能会导致剩余数据量过小，误差很大。
所以可以用均值、众数或者中位数来替换NaN值。 
具体视情况而定。譬如在用0，1代替男，女的性别列里，取均值显然没有任何意义。

```python
#  均值
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mean()
df["ST_NUM"].fillna(x, inplace = True)
```

```python
#  中位数
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].median()
df["ST_NUM"].fillna(x, inplace = True)
```

```python
#  众数
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mode()
df["ST_NUM"].fillna(x, inplace = True)
```

以下是删除重复行的方法：
```python
persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(persons)
df.drop_duplicates(inplace = True)
```

其他的数据预处理步骤最好用更加专业的库来完成。


## pandas统计


函数	        说明	        示例
count()	        非空值数量	    df["年龄"].count()
sum()	        求和	        df["薪资"].sum()
mean()	        平均值	        df["年龄"].mean()
median()	    中位数	        df["年龄"].median()
std()	        标准差	        df["绩效"].std()
var()	        方差	        df["绩效"].var()
min() / max()	最小/最大值	    df["年龄"].min()
quantile()	    分位数	        df["薪资"].quantile(0.25)


## pandas的实际运用

### 生成一个student数据集
student包含学号Number，名字Name，年龄Age， 成绩Score

随机生成一个数据集，为了之后的数据清洗练习，让这个数据集模拟成未清洗数据，在里面随机插入异常值
异常包括以下类型：
- NaN
- 数据类型错误
- 边界溢出

随机抽取一些元素用NaN代替
用条件筛选索引来做：
m = 0-1的随机浮点数 < 0.1
student[m] = np.nan

生成乱码的思路：
首先在一个字母数组里随机抽取字母
然后通过循环生成一个长度为4的随机字符串
然后在Score里随机抽取元素，在后面拼接随机字符串

然后保存csv文件

### 数据清洗

数据清洗的思路是
把nan用一定数据替换或是把含nan的行删除
处理乱码/异常数据

具体用什么替换要视情况而定。
name里的nan最好直接删除或是手动填充数值，因为name列的均值、众数和中位数毫无意义
age里的nan值我用均值代替，这代表平均年龄的意思

接下来是异常数据的处理，我一开始想通过isinstance来判断数据类型，但是我忽略了在加入乱码之后Score列的数据类型变成了object
此时如果对其进行数据类型的判断，有可能之前的纯数的数据类型会由integer转变成string，所以用类型判断会导致结果全部是False，返回的是空数组
所以用强制类型转化来做，把所有的都转化为整型数据，如果某个元素是字符串，无法转化，它的值就会变成NaN
然后再替代NaN值即可

我用平均成绩来填充数据了