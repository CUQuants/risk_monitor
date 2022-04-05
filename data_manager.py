import os
import pandas as pd
import datetime as dt
import yfinance as yf

class DataManager:
    
    def __init__(self):
        
        self.fund_return, self.market_returns = get_market_returns()

def get_fund_holdings_remote():

    df = pd.read_html("https://docs.google.com/spreadsheets/d/1V06FshlK4Fcr_YQM65zAcQqHs6VRaH0OMWTDHW3cAXE/edit#gid=0")[0]
    print(df[df.columns[1]][0])
    tickers = df[df.columns[1]].dropna().to_list()[2:]
    tickers = tickers[:len(tickers) - 2]
   
    return tickers

def get_fund_holdings_local():

    partial_name = "Corporate-Positions"
    cwd_filenames = os.listdir(os.getcwd())
    
    for i in os.listdir(os.getcwd()):
       
        compare_name = i[0:len(partial_name)]
        if partial_name == compare_name:
           
            df = pd.read_csv(i)
            print(df.columns.values)
            df = df.reset_index()
            df.columns = df.iloc[0].to_list()
            df = df[1:len(df) - 2]
            tickers = df[df.columns[0]].to_list()
            
    return tickers

def get_fund_holdings():
    
    try:
        
        print("checking if fund holdings are in local directory")
        tickers = get_fund_holdings_local()
        print("fund holdings are held in directory")
        
    except:
        
        print("fund holdings are not in local directory retreiving them from google sheets")
        tickers = get_fund_holdings_remote()
        
    return tickers

def get_market_tickers_local():

    tickers = pd.read_csv("market_tickers.csv")["Symbol"].to_list()
    return tickers

def get_market_tickers_remote():

    tickers = pd.read_html("https://docs.google.com/spreadsheets/d/1UzyrletuVNBwwNiysCMgMAEIhn5I5PTJTGMRLluEc50/edit?usp=sharing")[0]
    tickers = tickers[tickers.columns[1]].dropna().to_list()[1:]
    
    return tickers

def get_market_tickers():
    
    try: 
        
        print("checking if market tickers are in local directory")
        tickers = get_market_tickers_local()
        print("market tickers are held in local directory")
        
    except:
        
        print("market tickers are not in local directory retreiving them from google sheets")
        tickers = get_fund_holdings_remote()
        
    return tickers

def get_market_returns():

    market_tickers = get_market_tickers()
    fund_tickers = get_fund_holdings()
    
    end_date = dt.date.today()
    start_date = dt.date(end_date.year - 1, end_date.month, end_date.day)
    
    fund_returns = yf.download(fund_tickers, start_date, end_date)['Adj Close'].pct_change().dropna()
    market_returns = yf.download(market_tickers, start_date, end_date)['Adj Close'].pct_change().dropna()

    return fund_returns, market_returns
