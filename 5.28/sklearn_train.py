from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


X, y = load_iris(return_X_y=True)       # 这里加载了鸢尾花数据集

# 把数据随机分成训练集和测试集
# test_size代表测试集所占的比例
# random_state用来固定随机结果，这样结果就能复现了
X_train, X_test, y_train, y_test = train_test_split(        
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()       # 建立一个标准化器

X_train = scaler.fit_transform(X_train)     # 统一尺度
X_test = scaler.transform(X_test)

model = LogisticRegression()        # 加载模型

model.fit(X_train, y_train)     # 拟合模型/训练模型

pred = model.predict(X_test)        # 测试模型

print(accuracy_score(y_test, pred))     # 评估数据，准确率