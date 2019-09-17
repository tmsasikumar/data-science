from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

basetable = pd.read_csv("basetable.csv")
X = basetable[["age", "gender_F", "time_since_last_gift"]]
y = basetable[["target"]]
#plt.style.use('seaborn-whitegrid')
df = basetable[["age","target"]]
df.plot.scatter(x='age', y='target', label = 'predict')
#df.plot(x='age', y='target', label='predict')
plt.xlim(0,100)
plt.ylim(0,1)
#ymarks=[i for i in range(1,1+1,1)]
#plt.yticks(ymarks)
plt.show()
