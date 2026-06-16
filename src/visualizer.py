"""
Visualizer Module
Handles all data visualization tasks
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from config.config import FIGURE_WIDTH, FIGURE_HEIGHT, VISUALIZATION_PATH
import os

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (FIGURE_WIDTH, FIGURE_HEIGHT)

# Ensure visualization directory exists
try:
    os.makedirs(VISUALIZATION_PATH, exist_ok=True)
except Exception:
    pass

def plot_stock_price(data, ticker):
    """
    Plot stock closing price over time
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    plt.plot(data.index, data['Close'], linewidth=2, label='Close Price')
    plt.title(f"{ticker} Stock Price Over Time", fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}{ticker}_price.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}{ticker}_price.png")
    plt.show()

def plot_correlation_heatmap(corr_matrix):
    """
    Plot correlation matrix as heatmap
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Stock Correlation Matrix', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}correlation_heatmap.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}correlation_heatmap.png")
    plt.show()

def plot_multiple_stocks(stocks_data):
    """
    Plot multiple stocks on same graph (normalized)
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    
    for ticker, data in stocks_data.items():
        normalized = data['Close'] / data['Close'].iloc[0] * 100
        plt.plot(data.index, normalized, label=ticker, linewidth=2)
    
    plt.title('Normalized Stock Price Comparison (1 Year)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Normalized Price (Base = 100)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}comparison_all_stocks.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}comparison_all_stocks.png")
    plt.show()

def plot_daily_returns(data, ticker):
    """
    Plot daily returns
    """
    returns = data['Close'].pct_change()
    
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    plt.plot(returns.index, returns, linewidth=1, alpha=0.7)
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.5)
    plt.title(f"{ticker} Daily Returns", fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Daily Return (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}{ticker}_returns.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}{ticker}_returns.png")
    plt.show()

def plot_model_comparison(results_df):
    """
    Plot model comparison
    """
    fig, axes = plt.subplots(2, 2, figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    
    axes[0, 0].bar(results_df['Model'], results_df['MAE'], color='steelblue')
    axes[0, 0].set_title('Mean Absolute Error (MAE)', fontweight='bold')
    axes[0, 0].set_ylabel('MAE ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    axes[0, 1].bar(results_df['Model'], results_df['RMSE'], color='coral')
    axes[0, 1].set_title('Root Mean Squared Error (RMSE)', fontweight='bold')
    axes[0, 1].set_ylabel('RMSE ($)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    axes[1, 0].bar(results_df['Model'], results_df['R2'], color='green')
    axes[1, 0].set_title('R² Score', fontweight='bold')
    axes[1, 0].set_ylabel('R² Score')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    axes[1, 1].bar(results_df['Model'], results_df['MAPE'], color='purple')
    axes[1, 1].set_title('Mean Absolute Percentage Error (MAPE)', fontweight='bold')
    axes[1, 1].set_ylabel('MAPE (%)')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.suptitle('Model Performance Comparison', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}model_comparison.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}model_comparison.png")
    plt.show()

def plot_predictions_vs_actual(y_test, y_pred, model_name, ticker='MSFT'):
    """
    Plot predicted vs actual prices
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    plt.plot(range(len(y_test)), y_test, label='Actual Price', linewidth=2)
    plt.plot(range(len(y_pred)), y_pred, label='Predicted Price', linewidth=2, alpha=0.7)
    plt.title(f"{model_name} - {ticker} Price Prediction", fontsize=16, fontweight='bold')
    plt.xlabel('Days', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{VISUALIZATION_PATH}{model_name.replace(' ', '_')}_predictions.png", dpi=300)
    print(f"Saved plot: {VISUALIZATION_PATH}{model_name.replace(' ', '_')}_predictions.png")
    plt.show()

if __name__ == "__main__":
    print("Visualizer module loaded successfully")