import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data(df,title="Stock Price"):
    ax = df.plot(title=title)
    ax.set_xlabel("Data")
    ax.set_ylabel("Price")
    plt.show()

def symbol_to_path(symbol, base_dir="Data"):
    return "Data/" + "{}.csv".format(str(symbol))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        path = symbol_to_path(symbol)
        dfTemp = pd.read_csv(path, index_col= "Date", parse_dates=True, usecols=['Date','Close Price'],
                            na_values=['nan'])
        dfTemp = dfTemp.rename(columns = {'Close Price': symbol})
        df=df.join(dfTemp)
        df = df.dropna()

    return df

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) -1 
    daily_returns.ix[0,:] = 0
    return daily_returns

def test_run():
    #Build dataFrame
    start_date = '2-May-2017'
    end_date = '28-Jul-2017'
    dates = pd.date_range(start_date, end_date)
    symbols = ['ADANIPOWER']
    df = get_data(symbols, dates)
    plot_data(df)
    #Compute Daily Returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns,title= "Daily Returns")
    #plot_data(daily_returns)
    daily_returns.hist()
    plt.show()

if __name__ == "__main__":
    test_run()