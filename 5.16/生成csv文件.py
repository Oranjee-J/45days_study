import pandas as pd
import numpy as np
import random


pt1 = ['Alice','Alan','Bella','Bob','Carol','Charlie','Doris','David','Emma','Edward','Freya','Fayde','Grace','George','Hanna','Hans','Ive','Iric','Joseph','Johny']
pt2 = ['Apple','Banana','Cloudberry','Blueberry','Cherry','Pear','Strawberry']
pt3 = ['Ape','Bear','Dolphin','Elephant','Goose']

major = ['Computer','Math','Coding','Database','AI']

n = 100

student = pd.DataFrame({
    'number': range(20260516000,20260516000 + n),
    'name': [
        random.choice(pt1) + ' '
        + random.choice(pt2) + ' '
        + random.choice(pt3)
        for _ in range(n)
    ] ,
    'age': np.random.randint(18,22,size = n),
    'major': [random.choice(major)for _ in range(n)],
    'score':np.random.randint(1,100,size = n)
})
student['grade'] = student['age']-17
student['pass or not'] = student['score'] >= 60

student = student[['number','name','age','grade','major','score','pass or not']]        # 双中括号生成的才是表格而非Series

# 设置一点nan值

mask = np.random.rand(len(student)) < 0.1  # 10%概率变NaN
student.loc[mask, "score"] = np.nan


# 设置不规范数据
student.loc[7, "major"] = "compueter"   # 拼写错误
student.loc[8, "major"] = "AI!!!"       # 奇怪符号
student.loc[9, "name"] = "  Bob  "      # 多空格


student.loc[5, "score"] = 999
student.loc[6, "score"] = -10

student.loc[10, "age"] = "twenty"
student.loc[11, "score"] = "N/A"

print(student)

student.to_csv('student.csv',index = False)

