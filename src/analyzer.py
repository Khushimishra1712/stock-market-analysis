"""
Analyzer Module
Handles statistical analysis and correlation analysis
"""

import pandas as pd
import numpy as np
import sys
sys.path.append('.')
from config.config import PRIMARY_STOCK

def calculate_correlation_matrix(stocks_data):
    """
    Calculate correlation matrix between stocks
    """
    print(f"\nCalculating correlation matrix...")
    
    close_prices = pd.DataFrame()
    for ticker, data in stocks_data.items():
        close_prices[ticker] = data['Close']
    
    corr_matrix = close_prices.corr()
    print("✅ Correlation matrix calculated")
    
    return corr_matrix

def get_stock_statistics(data, ticker):
    """
    Calculate descriptive statistics for a stock
    """
    stats = {
        'Ticker': ticker,
        'Mean_Close': data['Close'].mean(),
        'Median_Close': data['Close'].median(),
        'Std_Dev': data['Close'].std(),
        'Min_Price': data['Close'].min(),
        'Max_Price': data['Close'].max(),
        'Price_Range': data['Close'].max() - data['Close'].min(),
        'Daily_Return_Mean': data['Close'].pct_change().mean(),
        'Daily_Return_Std': data['Close'].pct_change().std(),
        'Total_Volume': data['Volume'].sum(),
        'Avg_Volume': data['Volume'].mean()
    }
    return stats

def get_all_stocks_statistics(stocks_data):
    """
    Get statistics for all stocks
    """
    print(f"\nCalculating statistics for all stocks...")
    
    stats_list = []
    for ticker, data in stocks_data.items():
        stats = get_stock_statistics(data, ticker)
        stats_list.append(stats)
    
    stats_df = pd.DataFrame(stats_list)
    print("✅ Statistics calculated")
    
    return stats_df

def calculate_daily_returns(data):
    """
    Calculate daily returns for a stock
    """
    return data['Close'].pct_change()

def calculate_volatility(data, window=20):
    """
    Calculate rolling volatility
    """
    returns = calculate_daily_returns(data)
    volatility = returns.rolling(window=window).std()
    return volatility

def identify_correlations(corr_matrix, threshold=0.7):
    """
    Identify highly correlated stock pairs
    """
    correlated_pairs = []
    
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                correlated_pairs.append({
                    'Stock1': corr_matrix.columns[i],
                    'Stock2': corr_matrix.columns[j],
                    'Correlation': corr_matrix.iloc[i, j]
                })
    
    return correlated_pairs

if __name__ == "__main__":
    from data_loader import load_all_stocks
    from data_cleaner import clean_data
    
    stocks = load_all_stocks()
    clean_stocks = {k: clean_data(v, k) for k, v in stocks.items()}
    
    corr_matrix = calculate_correlation_matrix(clean_stocks)
    print(f"\nCorrelation Matrix:\n{corr_matrix}")
    
    stats = get_all_stocks_statistics(clean_stocks)
    print(f"\nStatistics:\n{stats}")