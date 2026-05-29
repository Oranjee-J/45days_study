from sklearn.linear_model import LogisticRegression

X = [
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 9],
    [9, 10],
    [10, 11]
]

y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)


print(model.predict([[4, 5]]))
print(model.predict_proba([[4, 5]]))