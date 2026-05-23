w = 10
lr = 0.1
loss = w ** 2

while loss > 0.0001:
    grad = 2*w      # 导数
    w = w - lr * grad
    loss = w ** 2
print(w)
# 0.009903520314283045

print(loss)

# 9.807971461541694e-05