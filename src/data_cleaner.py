"""
Data Cleaner Module
Handles data preprocessing and cleaning
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from config.config import PROCESSED_DATA_PATH

def clean_data(data, ticker):
    """
    Clean stock data by handling missing values and outliers
    
    Parameters:
    -----------
    data : pd.DataFrame
        Raw stock data
    ticker : str
        Stock symbol
        
    Returns:
    --------
    pd.DataFrame
        Cleaned data
    """
    print(f"\nCleaning {ticker} data...")
    
    df = data.copy()
    
    # Check for missing values
    missing_before = df.isnull().sum().sum()
    print(f"Missing values before: {missing_before}")
    
    # Fill missing values using forward fill then backward fill (compatible with pandas 3.x)
    df = df.ffill().bfill()
    
    missing_after = df.isnull().sum().sum()
    print(f"Missing values after: {missing_after}")
    
    # Remove duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Removing {duplicates} duplicate rows")
        df = df[~df.duplicated()]
    
    # Sort by date
    df = df.sort_index()
    
    print(f"✅ Cleaned data shape: {df.shape}")
    return df

def create_features(data):
    """
    Create additional features for modeling
    """
    df = data.copy()
    
    df['Daily_Return'] = df['Close'].pct_change()
    df['Price_Range'] = df['High'] - df['Low']
    df['Price_Change'] = df['Close'] - df['Open']
    df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
    
    for lag in [1, 2, 3, 5]:
        df[f'Close_Lag_{lag}'] = df['Close'].shift(lag)
    
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    
    df['Volatility'] = df['Daily_Return'].rolling(window=20).std()
    
    df = df.dropna()
    
    return df

def normalize_data(data, columns=None):
    """
    Normalize data using StandardScaler
    """
    df = data.copy()
    
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    
    return df, scaler

def prepare_data_for_modeling(data, test_split=0.8):
    """
    Prepare data for machine learning models
    """
    df = data.copy()
    
    X = df.drop(['Close', 'Adj Close'], axis=1, errors='ignore')
    y = df['Close']
    
    split_index = int(len(X) * test_split)
    
    X_train = X[:split_index]
    X_test = X[split_index:]
    y_train = y[:split_index]
    y_test = y[split_index:]
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    from data_loader import load_single_stock
    from config.config import PRIMARY_STOCK
    
    data = load_single_stock(PRIMARY_STOCK)
    cleaned_data = clean_data(data, PRIMARY_STOCK)
    featured_data = create_features(cleaned_data)
    print(f"\nFeatured data shape: {featured_data.shape}")
    print(f"\nFeatures created: {featured_data.columns.tolist()}")