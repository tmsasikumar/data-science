import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import quandl

ticker = 'TATAPOWER'
data = pd.DataFrame()
quandl.ApiConfig.api_key = "cLhcdoCHMuRLRhsmHLEf"
df = quandl.get("NSE/TATAPOWER",  rows=1000)
print (df[:10])
data[ticker] = df['Close']
log_returns = np.log(1 + data.pct_change())
#log_returns.tail()

data.plot(figsize=(10, 6));
#log_returns.plot(figsize = (10, 6))
meanValue = log_returns.mean()
variance = log_returns.var()
drift = meanValue - (0.5 * variance)
stdev = log_returns.std()
t_intervals = 500
iterations = 10

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print drift.values
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

plt.figure(figsize=(10,6))
plt.plot(price_list)
plt.show()