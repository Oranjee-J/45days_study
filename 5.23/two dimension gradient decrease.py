X = 10

y = 10

lr = 0.2

Loss = X**2 + 2*(y**2)

while Loss > 0.01:
    X = X - lr*(2*X)

    y = y - lr*(4*y)

    Loss = X**2 + 2*(y**2)


print(X)
# 0.06046617599999997

print(y)
# 1.0239999999999973e-06

print(Loss)
# 0.003656158442160124