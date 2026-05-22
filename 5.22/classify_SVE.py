import numpy as np


X = np.random.randint(0,5,(6,2))

w = np.array([1.0, -1.0])  
b = -0.5   

def svm_predict(x):
    score = np.dot(w, x) + b
    if score >= 0:      # score = 0 就是决策边界！
        return 1
    else:
        return -1


for x in X:
    print(x, "->", svm_predict(x))