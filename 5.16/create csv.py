import pandas as pd
import numpy as np
import random

m = ['a','b','c','d','e','f','g','h','i']

n = ['1','2','3','4','5']

x = 10

data = pd.DataFrame({
    'Number':range(1,11),
    'Name':[random.choice(m) + ' ' + random.choice(n) for _ in range(x)],
    'Age': np.random.randint(8,13, size = 10) ,
    'Score': np.random.randint(40,100,size = 10)

    
})

data['Grade'] = data['Age'] - 7
data['pass?'] = data['Score'] >= 60


select = np.random.rand(len(data)) < 0.2

data.loc[select, 'Name'] = np.nan

s2 = np.random.rand(len(data)) < 0.2
data.loc[s2,'Age'] = np.nan



str_array = []

for i in range(3):
    random_num = np.random.randint(0,len(m),size = 4)
    random_str = ''
    for index in random_num:
        random_str += m[index]
    str_array.append(random_str)

for i in str_array:
    random_num = np.random.randint(0,x)
    data.loc[random_num, 'Score'] = str(data.loc[random_num, 'Score']) + i



data.to_csv('new_student.csv')    