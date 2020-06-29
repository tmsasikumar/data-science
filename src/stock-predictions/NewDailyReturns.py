import quandl
import matplotlib.pyplot as plt
import numpy as np

def plot_data(df,title="Daily Return"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_xlim([1, 1000])
    plt.show()


def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) -1
    #daily_returns.ix[0,:] = 0
    print daily_returns
    return daily_returns

quandl.ApiConfig.api_key = "cLhcdoCHMuRLRhsmHLEf"

df = quandl.get("NSE/ADANIPOWER",  rows=400)
daily_returns = compute_daily_returns(df['Close'])
#plot_data(daily_returns)


daily_returns.hist(range = [-0.2,0.2], bins = 20)
# ax = df.plot(title="Daliy Ret")
# ax.set_xlim([1, 20])
# ax.xticks(np.arange(1, 21, 1.0))
plt.show()