import pandas as pd
from sklearn import linear_model
from  sklearn import metrics as m
basetable = pd.read_csv("basetable.csv")

variables_1 = ['age']
variables_2 = ["age", "time_since_last_gift"]
X_1 = basetable[variables_1]
X_2 = basetable[variables_2]
y = basetable[["target"]]

logreg = linear_model.LogisticRegression()

logreg.fit(X_1, y)
predictions_1 = logreg.predict_proba(X_1)[:, 1]
auc_1 = m.roc_auc_score(y, predictions_1)

# Make next prediction with second variable
logreg.fit(X_2, y)
predictions_2 = logreg.predict_proba(X_2)[:, 1]
auc_2 = m.roc_auc_score(y, predictions_2)

# Print auc_1 and auc_2
print(round(auc_1, 2))
print(round(auc_2, 2))
