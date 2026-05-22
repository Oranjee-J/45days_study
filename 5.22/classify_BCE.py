import numpy as np

p = np.random.uniform(0, 1, 10)



def classify_CE(x):
    m = 0
    for i in range(0,len(x)):
        if x[i] == 0:
            m = m - np.log(1-p[i])
        elif x[i] == 1:
            m = m - np.log(p[i])
    
    return m

x = [1,1,1,1,1,0,0,1,0,1]

print(classify_CE(x))
