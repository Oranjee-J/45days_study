import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# 前五行
print(df.head())
'''
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True

'''


# 维度
print(df.shape)
# (891, 15)
# Titanic 数据集共包含 891 条样本和 15 个特征。


# 字段信息
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
None
'''
''' 
特征包括：
- 数值型特征：age、fare、sibsp、parch 等
- 类别型特征：sex、embarked、class 等
- 布尔型特征：adult_male、alone
'''

# 统计信息
print(df.describe())
'''
         survived      pclass  ...       parch        fare
count  891.000000  891.000000  ...  891.000000  891.000000
mean     0.383838    2.308642  ...    0.381594   32.204208
std      0.486592    0.836071  ...    0.806057   49.693429
min      0.000000    1.000000  ...    0.000000    0.000000
25%      0.000000    2.000000  ...    0.000000    7.910400
50%      0.000000    3.000000  ...    0.000000   14.454200
75%      1.000000    3.000000  ...    0.000000   31.000000
max      1.000000    3.000000  ...    6.000000  512.329200

[8 rows x 6 columns]
'''

# 缺失值
print(df.isnull().sum())
'''
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
'''

'''
deck 缺失率极高（约77%），后续考虑删除。
age 存在较多缺失值，需要填补。
embarked 和 embark_town 仅有少量缺失，可采用众数填补。
'''

sns.countplot(
    x="sex",
    hue="survived",
    data=df
)
plt.show()
# 女性存活概率高于男性


sns.countplot(
    x="pclass",
    hue="survived",
    data=df
)
plt.show()
# 高等级船舱乘客存活概率更高


sns.boxplot(
    x="survived",
    y="age",
    data=df
)
plt.show()
# 幸存者票价整体高于死亡者


sns.boxplot(
    x="survived",
    y="fare",
    data=df
)
plt.show()
# 年轻人存活概率更高，但是影响程度低于性别和船舱等级