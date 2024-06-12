import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pmdarima as pm
import yfinance as yf

from arch import arch_model
from pmdarima.model_selection import train_test_split
from scipy.stats import chi2, jarque_bera
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import acf, adfuller
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.arima.model import ARIMA

def mcleod_li_test(x, k):
    """
    Calculates the McLeod-Li test statistic for a time series with k lags.
    Returns the test statistic and its p-value.
    """
    n = len(x)
    x_sq = x ** 2
    x_sum = np.sum(x_sq)
    x_lag_sum = np.sum(x_sq[:-k])
    test_stat = n * (n + 2) * x_lag_sum / (x_sum ** 2)
    df = k
    p_value = 1 - chi2.cdf(test_stat, df)
    return test_stat, p_value

if __name__ == '__main__':
    # Data import
    spy = yf.Ticker("SPY")
    hist = spy.history(start="2010-01-04", end="2020-02-01")
    df = pd.DataFrame(hist, columns=['Close'])

    # Convert prices to log returns
    df['Return'] = np.pad(np.diff(np.log(df['Close'])) * 100, (1, 0), 'constant', constant_values=np.nan)

    # Fit GARCH (1,1)
    diff_ts = df['Return'].iloc[1:]
    abs_returns = diff_ts.abs()

    y_train, y_test = train_test_split(abs_returns, train_size=0.8)

    garch_mod = arch_model(y_train, mean="Zero", vol='Garch', p=1, q=1, rescale=False)
    res_garch = garch_mod.fit()

    # N-step ahead forecast
    yhat = res_garch.forecast(horizon=y_test.shape[0], reindex=True)

    # One-step rolling forecast
    rolling_preds = []

    for i in range(y_test.shape[0]):
        train = abs_returns[:-(y_test.shape[0] - i)]
        model = arch_model(train, p=1, q=1, rescale=False)
        model_fit = model.fit(disp='off')
        # One step ahead predictor
        pred = model_fit.forecast(horizon=1, reindex=True)
        rolling_preds.append(np.sqrt(pred.variance.values[-1, :][0]))

    rolling_preds = pd.Series(rolling_preds, index=y_test.index)

    # Model diagnostics - Jarque-Bera test
    std_resid = res_garch.resid / res_garch.conditional_volatility
    jb_test = jarque_bera(std_resid)
    print("Jarque-Bera test statistic:", jb_test[0])
    print("p-value:", jb_test[1])
