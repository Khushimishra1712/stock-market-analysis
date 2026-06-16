"""
Data Loader Module
Handles downloading and loading stock data from Yahoo Finance
"""

import yfinance as yf
import pandas as pd
import sys
sys.path.append('.')
from config.config import START_DATE, END_DATE, PRIMARY_STOCK, ALL_STOCKS, RAW_DATA_PATH

def download_stock_data(ticker, start_date=START_DATE, end_date=END_DATE):
    """
    Download historical stock data from Yahoo Finance
    
    Parameters:
    -----------
    ticker : str
        Stock symbol (e.g., 'MSFT', 'AAPL')
    start_date : datetime
        Start date for data
    end_date : datetime
        End date for data
        
    Returns:
    --------
    pd.DataFrame
        Historical stock data with columns: Open, High, Low, Close, Volume, Adj Close
    """
    print(f"Downloading {ticker} data from {start_date.date()} to {end_date.date()}...")
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        print(f"✅ Successfully downloaded {len(data)} records for {ticker}")
        return data
    except Exception as e:
        print(f"❌ Error downloading {ticker}: {str(e)}")
        return None

def load_all_stocks(start_date=START_DATE, end_date=END_DATE):
    """
    Download data for all stocks in the analysis
    
    Returns:
    --------
    dict
        Dictionary with stock symbols as keys and DataFrames as values
    """
    print(f"\n{'='*60}")
    print("LOADING STOCK DATA")
    print(f"{'='*60}\n")
    
    stocks_data = {}
    for stock in ALL_STOCKS:
        data = download_stock_data(stock, start_date, end_date)
        if data is not None:
            stocks_data[stock] = data
    
    print(f"\n✅ Loaded data for {len(stocks_data)} stocks")
    return stocks_data

def load_single_stock(ticker, start_date=START_DATE, end_date=END_DATE):
    """
    Load data for a single stock
    
    Parameters:
    -----------
    ticker : str
        Stock symbol
        
    Returns:
    --------
    pd.DataFrame
        Stock data
    """
    return download_stock_data(ticker, start_date, end_date)

def save_data_to_csv(data_dict, output_path=RAW_DATA_PATH):
    """
    Save downloaded data to CSV files
    
    Parameters:
    -----------
    data_dict : dict
        Dictionary of stock data
    output_path : str
        Path to save CSV files
    """
    for ticker, data in data_dict.items():
        file_path = f"{output_path}{ticker}_data.csv"
        data.to_csv(file_path)
        print(f"Saved {ticker} data to {file_path}")

if __name__ == "__main__":
    stocks = load_all_stocks()
    print(f"\nLoaded stocks: {list(stocks.keys())}")
    print(f"\nMSFT data shape: {stocks[PRIMARY_STOCK].shape}")
    print(f"\nFirst few rows of MSFT data:\n{stocks[PRIMARY_STOCK].head()}")