Titanic_Project/
│
├── eda.py
├── feature_engineering.py
├── model.py                  # 明天创建
├── menu.md
└── titanic_processed.csv


# Titanic Survival Prediction Project

## Dataset Description

数据集包含891条乘客记录。
主要特征包含：
'survived'：是否存活
'pclass'：船舱等级
'age'：年龄
'sibsp'：兄弟姐妹/配偶数量
'parch'：父母/子女数量
'fare'：船票价格
'embarked'：登船港口

## EDA

数据概况：
Titanic 数据集共包含 891 条样本和 15 个特征

缺失值分析：
deck缺失688条
age缺失177条
embarked缺失2条

主要发现：
- 女性存活概率高于男性
现实依据：泰坦尼克救援过程中遵循‘妇女儿童优先’的原则，因此女性乘客生存率更高
- 高等级船舱乘客存活概率更高
现实依据：头等舱乘客的经济地位和社会地位更高，救援优先级更高，因此生存率也更高
- 票价较高的乘客生存率
现实依据：同上
- 存活者平均年龄更年轻
现实依据：一是儿童被优先救援，二是泰坦尼克失事海域海水冰冷，年轻人身体强壮，生存率更高。

## 特征工程

1. 删除特征：
- alive
- deck
- class
- embark_town
- adult_male
- who

2. 缺失值处理
- age使用中位数填补（因为age的极端值较多
- embarked使用众数填补（因为港口的众数表现人流量较大的港口

3. 特征构造
FamilySize = sibsp + parch + 1
显然独自出行与跟家人一起出行两类对比更显著，有无家人陪同对存活率影响较大。
