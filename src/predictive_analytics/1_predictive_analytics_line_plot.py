import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("basetable.csv")
df = dataframe.loc[dataframe['target'] == 1]

df.groupby('age').count().plot(legend=None)

plt.show()
print(df)
print(len(df))
