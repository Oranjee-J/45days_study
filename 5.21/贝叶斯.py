from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. 训练数据

texts = [
    "免费领取大奖",
    "点击获得优惠",
    "限时免费优惠",
    "今天开会",
    "项目进度汇报",
    "明天提交作业"
]

# 1 = 垃圾邮件
# 0 = 正常邮件

labels = [1, 1, 1, 0, 0, 0]


# 2. 文本转数字

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

# 查看有哪些词
print("词汇表：")
print(vectorizer.get_feature_names_out())

print()

# 查看向量化结果
print("文本向量：")
print(X.toarray())

print()


# 3. 创建贝叶斯模型

model = MultinomialNB()

# 训练模型
model.fit(X, labels)


# 4. 新文本预测

new_text = ["免费优惠领取"]

# 转换成向量
X_new = vectorizer.transform(new_text)

# 预测类别
prediction = model.predict(X_new)

# 预测概率
probability = model.predict_proba(X_new)


# 5. 输出结果

print("新文本：", new_text[0])

print()

if prediction[0] == 1:
    print("预测结果：垃圾邮件")
else:
    print("预测结果：正常邮件")

print()

print("属于正常邮件的概率：", probability[0][0])
print("属于垃圾邮件的概率：", probability[0][1])