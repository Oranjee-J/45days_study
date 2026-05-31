from sklearn.datasets import load_wine
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report

wine = load_wine()
X = wine.data
y = wine.target
X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3
)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test,y_pred)

print(f'accuracy: {acc:4f}')
print('Classification Report:\n')
print(classification_report(y_test,y_pred,target_names=wine.target_names))



feature_names = wine.feature_names
importances = model.feature_importances_

feature_importance_pairs = list(
    zip(feature_names, importances)
)

sorted_features = sorted(
    feature_importance_pairs,
    key=lambda x: x[1],
    reverse=True
)

print("Top 5 Important Features:")

for feature, importance in sorted_features[:5]:
    print(
        f"{feature}: {importance:.4f}"
    )




