import pandas as pd
import numpy as np

student = pd.read_csv('new_student.csv',index_col = 0)

# 把name是nan的行全部删除
st1 = student.dropna(subset = 'Name').copy()

# 把age里的nan替换成均值
st2 = st1.copy()
age_mean = round(st2['Age'].mean(),2)
st2['Age'] = st2['Age'].fillna(age_mean)

# Score里存在字符串，数据类型是object，不能用这个数据来取均值和判断类型，所以强制把里面数据类型转化成数值数据类型，如果数据是字符串会变成nan
# 然后用均值替换nan值
st3 = st2.copy()
st3['Score'] = pd.to_numeric(st3['Score'],errors='coerce')
score_mean = round(st3['Score'].mean(),2)
st3['Score'] = st3['Score'].fillna(score_mean)

st3.to_csv('student_after_clean.csv')
