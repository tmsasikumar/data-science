import quandl
import matplotlib.pyplot as plt
import talib as ta
from talib import MA_Type
from mpl_finance import candlestick2_ohlc

quandl.ApiConfig.api_key = "cLhcdoCHMuRLRhsmHLEf"
df = quandl.get("NSE/VOLTAS",  rows=100)
fig, ax = plt.subplots()
candlestick2_ohlc(ax,df['Open'],df['High'],df['Low'],df['Close'],width=0.6,colorup='g', colordown='r')

upper, middle, lower = ta.BBANDS(df.Close.values, matype=MA_Type.T3)

#plt.figure(figsize=(10,6))
plt.plot(upper, 'b', label='Upper Band')
plt.plot(lower,'y', label='Lower Band')
plt.legend(loc='upper left')
plt.show()