import numpy as np
X = np.array([1,2,3,4,5,6,7,8,9],dtype = float)
y = np.array([2,4,6,8,10,12,14,16,18],dtype=float)

w = 0.0
b = 0.0

lr = 0.01

for epoch in range(0,1000):
    y_pred = w*X + b
    loss = np.mean((y_pred-y)**2)

    dw = np.mean(2*(y_pred - y) * X)
    db = np.mean(2*(y_pred - y))

    w = w - lr*dw
    b = b - lr*db


print(w,b)