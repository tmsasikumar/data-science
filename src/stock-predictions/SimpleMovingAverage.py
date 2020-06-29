import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
import talib as ta
from mpl_finance  import candlestick2_ohlc

#
# SUN PHARMA
#

quandl.ApiConfig.api_key = "cLhcdoCHMuRLRhsmHLEf"
share_name = "VOLTAS"
df = quandl.get("NSE/%s" % share_name, rows=100)
fig, ax = plt.subplots()
candlestick2_ohlc(ax,df['Open'],df['High'],df['Low'],df['Close'],width=0.6,colorup='g', colordown='r')

arr = np.array(pd.DataFrame(df.Close))
#print arr
short_sma = ta.SMA(df.Close.values, timeperiod = 5)
long_sma = ta.SMA(df.Close.values, timeperiod = 50)
#print BATA
plt.plot(short_sma, 'b', label='Short SMA')
plt.plot(long_sma,'y', label='Long SMA')
plt.title(share_name)
plt.legend(loc='upper left')
plt.show()