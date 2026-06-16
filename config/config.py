"""
Configuration file for Stock Market Analysis Project
Modify these settings to customize the analysis
"""

import pandas as pd
from datetime import datetime, timedelta
import os

# ==================== DATE CONFIGURATION ====================
# Set the analysis period (1 year back from today)
END_DATE = datetime.now()
START_DATE = END_DATE - timedelta(days=365)

# ==================== STOCK SYMBOLS ====================
# Primary stock to analyze
PRIMARY_STOCK = 'MSFT'

# Comparison stocks for correlation analysis
COMPARISON_STOCKS = ['AAPL', 'GOOGL', 'NVDA', 'TSLA']

# All stocks combined
ALL_STOCKS = [PRIMARY_STOCK] + COMPARISON_STOCKS

# ==================== MODEL CONFIGURATION ====================
# Train-test split ratio
TRAIN_TEST_SPLIT = 0.8

# Look-back period for creating lag features (days)
LOOKBACK_PERIOD = 10

# Test set size
TEST_SIZE = int(len(pd.date_range(START_DATE, END_DATE, freq='D')) * (1 - TRAIN_TEST_SPLIT))

# ==================== TECHNICAL INDICATORS ====================
# RSI period (Relative Strength Index)
RSI_PERIOD = 14

# MACD parameters
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# Bollinger Bands
BB_PERIOD = 20
BB_STD = 2

# Simple Moving Averages
SMA_SHORT = 20
SMA_LONG = 50

# ==================== VISUALIZATION CONFIGURATION ====================
# Figure size for plots
FIGURE_WIDTH = 14
FIGURE_HEIGHT = 6

# Color scheme
COLOR_PRIMARY = '#1f77b4'  # Blue
COLOR_SECONDARY = '#ff7f0e'  # Orange
COLOR_SUCCESS = '#2ca02c'  # Green
COLOR_DANGER = '#d62728'  # Red

# ==================== OUTPUT PATHS ====================
RAW_DATA_PATH = 'data/raw/'
PROCESSED_DATA_PATH = 'data/processed/'
VISUALIZATION_PATH = 'visualizations/'
REPORT_PATH = 'reports/'

# ==================== RANDOM STATE ====================
# For reproducibility
RANDOM_STATE = 42


def ensure_output_dirs():
	"""Create output directories defined in this config if they don't exist."""
	for p in (RAW_DATA_PATH, PROCESSED_DATA_PATH, VISUALIZATION_PATH, REPORT_PATH):
		try:
			os.makedirs(p, exist_ok=True)
		except Exception:
			pass


def _print_summary():
	print("\n✅ Configuration loaded successfully!")
	print(f"Primary Stock: {PRIMARY_STOCK}")
	print(f"Comparison Stocks: {COMPARISON_STOCKS}")
	print(f"Analysis Period: {TRAIN_TEST_SPLIT*100:.0f}% train, {(1-TRAIN_TEST_SPLIT)*100:.0f}% test")


if __name__ == "__main__":
	_print_summary()
	ensure_output_dirs()