from sklearn import linear_model
import pandas as pd

basetable = pd.read_csv("basetable.csv")
X = basetable[['age', 'gender_F', 'time_since_last_gift']]
print(len(basetable))

y = basetable[['target']]

logreg = linear_model.LogisticRegression()
logreg.fit(X, y)
print(logreg.coef_)
print(logreg.intercept_)

predictors = ["age", "gender_F", "time_since_last_gift"]
X = basetable[predictors]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Assign the coefficients to a list coef
coef = logreg.coef_
print (coef)
for p, c in zip(predictors, list(coef[0])):
    print(p + '\t' + str(c))

# Assign the intercept to the variable intercept
intercept = logreg.intercept_
print(intercept)

new_data = basetable[["age","gender_F", "time_since_last_gift"]]

# Make a prediction for each observation in new_data and assign it to predictions
predictions = logreg.predict_proba(new_data)
basetable['no_proba'] = predictions[:, 0]
basetable['yes_proba'] = predictions[:, 1]
print(basetable)

