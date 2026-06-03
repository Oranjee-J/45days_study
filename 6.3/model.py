from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.metrics import confusion_matrix

df = pd.read_csv('titanic_processed.csv')

X = df.drop(
    "survived",
    axis=1
)
y = df["survived"]
print(X.columns)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
results = []

lr = LogisticRegression(
    max_iter=1000,
    random_state=42
)
lr.fit(X_train,y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test,lr_pred)
lr_prec = precision_score(y_test,lr_pred)
lr_recall = recall_score(y_test,lr_pred)
lr_f1 = f1_score(y_test,lr_pred)

results.append([
    "Logistic Regression",
    lr_acc,
    lr_prec,
    lr_recall,
    lr_f1
])


rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf.fit(X_train,y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test,rf_pred)
rf_prec = precision_score(y_test,rf_pred)
rf_recall = recall_score(y_test,rf_pred)
rf_f1 = f1_score(y_test,rf_pred)
results.append([
    "Random Forest Classifier",
    rf_acc,
    rf_prec,
    rf_recall,
    rf_f1
])

gb = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)
gb.fit(X_train, y_train)
gb_pred = gb.predict(X_test)
gb_acc = accuracy_score(y_test, gb_pred)
gb_prec = precision_score(y_test,gb_pred)
gb_recall = recall_score(y_test,gb_pred)
gb_f1 = f1_score(y_test,gb_pred)
results.append([
    "Gradient Boosting Classifier",
    gb_acc,
    gb_prec,
    gb_recall,
    gb_f1
])

result_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print(result_df)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)
print(importance)

# 调参
param_grid = {
    'n_estimators': [50,100,200],
    'max_depth':[3,5,7,None],
    'min_samples_split':[2,5,10]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1'
)

grid.fit(X_train,y_train)

print('the best param is:', grid.best_params_)
print('the best score is:', grid.best_score_)

error_df = X_test.copy()

error_df["true"] = y_test.values
error_df["pred"] = rf_pred

errors = error_df[
    error_df["true"] != error_df["pred"]
]
print(errors.head())
print(
    confusion_matrix(
        y_test,
        rf_pred
    )
)