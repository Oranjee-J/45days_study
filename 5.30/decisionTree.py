from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X = [
    [25, 5000],
    [35, 10000],
    [45, 15000],
    [20, 3000],
    [50, 20000]
]

# 标签
y = [0, 1, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)

print(acc)  # 这里不是0就是1，因为测试集太小了