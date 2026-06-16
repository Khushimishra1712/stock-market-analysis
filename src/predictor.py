"""
Predictor Module
Builds and evaluates machine learning models for stock price prediction
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings('ignore')

from config.config import RANDOM_STATE

class StockPredictor:
    """
    Class for building and evaluating stock price prediction models
    """
    
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def build_linear_regression(self, X_train, y_train, X_test, y_test):
        """
        Build Linear Regression model
        """
        print("\nBuilding Linear Regression model...")
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        metrics = self._calculate_metrics(y_test, y_pred, 'Linear Regression')
        self.models['Linear Regression'] = model
        self.results['Linear Regression'] = {'predictions': y_pred, 'metrics': metrics}
        
        return model, metrics
    
    def build_random_forest(self, X_train, y_train, X_test, y_test, n_estimators=100):
        """
        Build Random Forest model
        """
        print("\nBuilding Random Forest model...")
        model = RandomForestRegressor(n_estimators=n_estimators, 
                                     random_state=RANDOM_STATE,
                                     n_jobs=-1)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        metrics = self._calculate_metrics(y_test, y_pred, 'Random Forest')
        self.models['Random Forest'] = model
        self.results['Random Forest'] = {'predictions': y_pred, 'metrics': metrics}
        
        return model, metrics
    
    def build_xgboost(self, X_train, y_train, X_test, y_test):
        """
        Build XGBoost model
        """
        print("\nBuilding XGBoost model...")
        model = xgb.XGBRegressor(n_estimators=100,
                               learning_rate=0.1,
                               max_depth=5,
                               random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        metrics = self._calculate_metrics(y_test, y_pred, 'XGBoost')
        self.models['XGBoost'] = model
        self.results['XGBoost'] = {'predictions': y_pred, 'metrics': metrics}
        
        return model, metrics
    
    def build_arima(self, data, order=(5, 1, 2)):
        """
        Build ARIMA model for time series
        """
        print("\nBuilding ARIMA model...")
        try:
            model = ARIMA(data, order=order)
            fitted_model = model.fit()
            
            print("✅ ARIMA model fitted successfully")
            self.models['ARIMA'] = fitted_model
            
            return fitted_model
        except Exception as e:
            print(f"❌ ARIMA model failed: {str(e)}")
            return None
    
    def _calculate_metrics(self, y_true, y_pred, model_name):
        """
        Calculate evaluation metrics
        """
        # Ensure inputs are 1-D numpy arrays
        y_true_arr = np.ravel(np.array(y_true))
        y_pred_arr = np.ravel(np.array(y_pred))

        mae = mean_absolute_error(y_true_arr, y_pred_arr)
        rmse = np.sqrt(mean_squared_error(y_true_arr, y_pred_arr))
        r2 = r2_score(y_true_arr, y_pred_arr)

        # MAPE: avoid division by zero by masking zero true values
        with np.errstate(divide='ignore', invalid='ignore'):
            mask = y_true_arr != 0
            if mask.any():
                mape = np.mean(np.abs((y_true_arr[mask] - y_pred_arr[mask]) / y_true_arr[mask])) * 100
            else:
                mape = np.nan
        
        metrics = {
            'MAE': mae,
            'RMSE': rmse,
            'R2': r2,
            'MAPE': mape
        }
        
        print(f"{model_name} Metrics:")
        print(f"  MAE: ${mae:.2f}")
        print(f"  RMSE: ${rmse:.2f}")
        print(f"  R² Score: {r2:.4f}")
        print(f"  MAPE: {mape:.2f}%")
        
        return metrics
    
    def get_best_model(self):
        """
        Get the best performing model based on R² score
        """
        best_model_name = max(self.results.keys(), 
                             key=lambda x: self.results[x]['metrics']['R2'])
        best_r2 = self.results[best_model_name]['metrics']['R2']
        
        print(f"\n🏆 Best Model: {best_model_name} (R² = {best_r2:.4f})")
        
        return best_model_name, self.models[best_model_name]
    
    def get_results_summary(self):
        """
        Get summary of all model results
        """
        summary = []
        for model_name, result in self.results.items():
            summary.append({
                'Model': model_name,
                'MAE': result['metrics']['MAE'],
                'RMSE': result['metrics']['RMSE'],
                'R2': result['metrics']['R2'],
                'MAPE': result['metrics']['MAPE']
            })
        
        return pd.DataFrame(summary).sort_values('R2', ascending=False)

if __name__ == "__main__":
    print("Predictor module loaded successfully")