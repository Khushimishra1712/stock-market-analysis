# Stock Market Analysis & Predictive Modeling Project

## 📊 Project Overview

This is an **end-to-end data science project** that analyzes Microsoft (MSFT) stock data over 1 year, performs correlation analysis with other tech stocks, and builds multiple predictive models to forecast stock prices.

### Key Features:
- ✅ Real-time data collection from Yahoo Finance
- ✅ Exploratory Data Analysis (EDA)
- ✅ Correlation analysis across 5 tech stocks
- ✅ 5 different predictive models (Linear Regression, Random Forest, XGBoost, ARIMA, Exponential Smoothing)
- ✅ Technical indicators (RSI, MACD, Bollinger Bands)
- ✅ Comprehensive visualizations
- ✅ Model evaluation and comparison

---

## 🎯 Project Objectives

1. **Data Collection & Exploration:** Gather 1 year of historical MSFT stock data
2. **Correlation Analysis:** Understand relationships between MSFT and other tech stocks (AAPL, GOOGL, NVDIA, TSLA)
3. **Predictive Modeling:** Build and compare multiple ML models to forecast MSFT stock prices
4. **Technical Analysis:** Calculate technical indicators for trading insights
5. **Insights & Visualization:** Create professional visualizations and actionable insights

---

## 📁 Project Structure

```
stock-market-analysis/
├── data/
│   ├── raw/                    # Raw downloaded stock data
│   ├── processed/              # Cleaned and processed data
│   └── sample_data.csv         # Sample dataset
├── notebooks/
│   ├── 01_EDA.ipynb           # Exploratory Data Analysis
│   ├── 02_Correlation_Analysis.ipynb  # Stock correlation analysis
│   ├── 03_Predictive_Modeling.ipynb   # ML model building
│   └── 04_Technical_Analysis.ipynb    # Technical indicators
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Data downloading and loading
│   ├── data_cleaner.py        # Data cleaning and preprocessing
│   ├── analyzer.py            # Statistical analysis functions
│   ├── predictor.py           # ML model building and evaluation
│   └── visualizer.py          # Visualization functions
├── visualizations/            # Output charts and plots
├── reports/                   # Analysis reports and findings
├── config/
│   └── config.py             # Configuration settings
├── requirements.txt           # Project dependencies
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

---

## 🚀 Getting Started

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation:

1. **Clone the repository:**
```bash
git clone https://github.com/Khushimishra1712/stock-market-analysis.git
cd stock-market-analysis
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 📖 How to Use

### Step 1: Exploratory Data Analysis
```bash
jupyter notebook notebooks/01_EDA.ipynb
```
- Explore MSFT stock data trends
- Visualize price movements and volume
- Understand data distribution and statistics

### Step 2: Correlation Analysis
```bash
jupyter notebook notebooks/02_Correlation_Analysis.ipynb
```
- Analyze how MSFT correlates with AAPL, GOOGL, NVDIA, TSLA
- Create correlation heatmaps
- Identify patterns and relationships

### Step 3: Predictive Modeling
```bash
jupyter notebook notebooks/03_Predictive_Modeling.ipynb
```
- Build 5 different ML models
- Compare model performance
- Visualize predictions vs actual prices

### Step 4: Technical Analysis
```bash
jupyter notebook notebooks/04_Technical_Analysis.ipynb
```
- Calculate RSI (Relative Strength Index)
- Compute MACD (Moving Average Convergence Divergence)
- Plot Bollinger Bands
- Identify support and resistance levels

---

## 📊 Data Source

**yfinance** - Yahoo Finance API
- ✅ Real historical stock data
- ✅ No API keys required
- ✅ Covers MSFT + comparison stocks
- ✅ Last 1 year of trading data

**Stocks Analyzed:**
- Primary: Microsoft (MSFT)
- Comparison: Apple (AAPL), Google (GOOGL), NVIDIA (NVDIA), Tesla (TSLA)

---

## 🤖 Predictive Models Implemented

### 1. **Linear Regression**
- Baseline model for price prediction
- Assumes linear relationship between features and price

### 2. **Random Forest**
- Ensemble method capturing non-linear patterns
- Less prone to overfitting than single decision trees

### 3. **XGBoost**
- Advanced gradient boosting algorithm
- Excellent performance on time series data

### 4. **ARIMA** (AutoRegressive Integrated Moving Average)
- Time series specific model
- Captures temporal dependencies

### 5. **Exponential Smoothing**
- Weights recent data more heavily
- Good for trend-following predictions

---

## 📈 Model Evaluation Metrics

- **MAE** (Mean Absolute Error) - Average prediction error
- **RMSE** (Root Mean Squared Error) - Penalizes larger errors
- **R² Score** - How well the model fits the data (0-1 scale)
- **MAPE** (Mean Absolute Percentage Error) - Error as percentage

---

## 🔍 Key Findings (To Be Updated After Running)

After running the notebooks, you'll discover:
- Stock price trends over 1 year
- Correlation patterns between tech stocks
- Best performing predictive model
- Technical indicator signals
- Potential trading opportunities

---

## 📚 Libraries Used

- **Data Processing:** pandas, numpy
- **Machine Learning:** scikit-learn, xgboost, statsmodels
- **Time Series:** statsmodels (ARIMA)
- **Visualization:** matplotlib, seaborn, plotly
- **Data Fetching:** yfinance
- **Notebooks:** jupyter

---

## 💡 Key Insights Expected

1. **Correlation Insights:** Understanding which stocks move together
2. **Model Performance:** Which algorithm predicts best
3. **Price Patterns:** Identifying trends and seasonality
4. **Risk Analysis:** Volatility and variability in prices
5. **Trading Signals:** Technical indicators for decision making

---

## 🎓 Learning Outcomes

After completing this project, you'll understand:
- How to collect and process real-world financial data
- Exploratory data analysis techniques
- Correlation and statistical analysis
- Building and evaluating multiple ML models
- Time series forecasting methods
- Technical analysis indicators
- Data visualization best practices

---

## 🔧 Customization Options

You can easily modify the project:
- **Change time period:** Update `START_DATE` and `END_DATE` in config
- **Analyze different stocks:** Modify stock symbols in `config.py`
- **Adjust model parameters:** Fine-tune hyperparameters in `predictor.py`
- **Add more stocks:** Extend the correlation analysis
- **Create custom visualizations:** Use the visualizer module

---

## 📝 Project Status

- [x] Project structure created
- [x] Data loading module
- [x] Data cleaning module
- [x] Analysis functions
- [x] Prediction models
- [x] Visualization functions
- [ ] Run notebooks and gather results
- [ ] Interpret findings
- [ ] Customize and enhance

---

## 💼 Resume Impact

This project demonstrates:
- ✅ End-to-end data science workflow
- ✅ Real-world financial data handling
- ✅ Multiple ML algorithms implementation
- ✅ Data analysis and visualization skills
- ✅ Time series forecasting
- ✅ Statistical analysis
- ✅ GitHub version control
- ✅ Professional documentation

---

## 📞 Questions & Support

For any questions about the project:
1. Check the notebook comments
2. Review the module docstrings
3. Examine the config.py for settings
4. Refer to documentation in each module

---

## 📄 License

This project is open source and available for educational purposes.

---

**Last Updated:** June 2026  
**Author:** Khushimishra1712  
**Status:** Active Development

---

## Next Steps:

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Run Notebook 01: `jupyter notebook notebooks/01_EDA.ipynb`
3. ✅ Follow through Notebooks 02-04
4. ✅ Analyze results and create summary
5. ✅ Push to GitHub when complete

**Happy analyzing! 📊🚀**
