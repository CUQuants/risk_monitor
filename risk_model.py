import os
import pandas as pd
import datetime as dt
import yfinance as yf

'''
#for troubleshooting / developing
def dev_data_pull(symbols, prices_type):

    try:
        
        prices = pd.read_csv("{}_prices.csv".format(prices_type), index_col = 0)
        print("read from file")

    except: 
        
        end_date = dt.date.today()
        start_date = dt.date(end_date.year - 1, end_date.month, end_date.day)
        prices = yf.download(symbols, start_date, end_date)['Close']
        prices.to_csv("{}_prices.csv".format(prices_type))
        print("downloaded from yahoo")
    
    return prices

#for production
def prod_data_pull(symbols, prices_type):
    
    end_date = dt.date.today()
    start_date = dt.date(end_date.year - 1, end_date.month, end_date.day)
    prices = yf.download(symbols, start_date, end_date)['Close']
    prices.to_csv("{}_prices.csv".format(prices_type))
    
    return prices
'''

def get_fund_holdings_remote():

    df = pd.read_html("https://docs.google.com/spreadsheets/d/1V06FshlK4Fcr_YQM65zAcQqHs6VRaH0OMWTDHW3cAXE/edit#gid=0")[0]
    tickers = df[df.columns[1]].dropna().to_list()[2:]
    tickers = tickers[:len(tickers) - 2]
    
    return tickers

    
'''
symbols_df = pd.read_csv("tickers.csv")
symbols = symbols_df["Symbol"].to_list()
prices = dev_data_pull(symbols, "external")
'''

#fund_tickers = get_fund_holdings_remote()

partial_name = "Corporate-Positions"
cwd_filenames = os.listdir(os.getcwd())

for i in os.listdir(os.getcwd()):
    
    compare_name = i[0:len(partial_name)]
    if partial_name == compare_name:
        
        df = pd.read_csv(i)
        print(df.columns.values)