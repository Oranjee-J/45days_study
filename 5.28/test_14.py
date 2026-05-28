from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(len(X_train))     # 训练集是120条
print(len(X_test))      # 测试集时30条


model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(accuracy_score(y_test,pred))