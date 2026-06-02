import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

# 把可以推导，可能导致数据泄露的特征删除了
df.drop(
    columns=[
        "alive",
        "deck",
        "class",
        "embark_town",
        "adult_male",
        "who"
    ],
    inplace=True
)

# 用中位数填充年龄
df["age"] = df["age"].fillna(
    df["age"].median()
)

# 港口用出现数量最多的补
df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)

# 构造一个新的特征
df["FamilySize"] = (
    df["sibsp"]
    + df["parch"]
    + 1
)

df = pd.get_dummies(
    df,
    columns=["sex", "embarked"],
    drop_first=True
)

df["alone"] = df["alone"].astype(int)
print(df.columns)

df.to_csv(
    "titanic_processed.csv",
    index=False
)