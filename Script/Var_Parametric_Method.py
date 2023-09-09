import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def calculate_variance_covariance_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days):
    # Fetch historical prices
    prices = pd.DataFrame()
    for ticker in tickers:
        stock_data = yf.Ticker(ticker)
        stock_prices = stock_data.history(period='1d', start=start_date, end=end_date)['Close']
        prices[ticker] = stock_prices

    # Calculate daily returns
    returns = prices.pct_change().dropna()

    # Calculate portfolio returns
    portfolio_returns = returns.dot(weights)

    # Calculate mean and standard deviation of portfolio returns
    mean_return_daily = np.mean(portfolio_returns)
    std_return_daily = np.std(portfolio_returns)

    # Calculate mean and standard deviation for the specified time period
    mean_return = mean_return_daily * time_period_days
    std_return = std_return_daily * np.sqrt(time_period_days)

    # VaR calculation using Variance-Covariance method
    VaR = mean_return - std_return * norm.ppf(1 - confidence_interval)

    print(f"Value at Risk (VaR) at {confidence_interval * 100}% confidence level over {time_period_days} days is {VaR * 100:.2f}%")

    # Plotting the distribution of portfolio returns and the VaR
    plt.hist(portfolio_returns * 100, bins=50, density=True, alpha=0.75, label="Portfolio Returns")
    plt.axvline(-VaR * 100, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval * 100:.0f}% confidence level')
    plt.xlabel('Daily Return (Percentage)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Portfolio Daily Returns (Percentage) - Parametric Method')
    plt.legend()
    plt.show()

# Example usage
tickers = ['XLK', 'XLC', 'XLY', 'XLE', 'XLI', 'XLB', 'XLF', 'XLRE', 'XLP', 'XLU', 'XLV', 'FXI', 'GDX']
weights = [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.13, 0.1]
start_date = '2018-08-10'
end_date = '2023-08-10'
confidence_interval = 0.95
time_period_days = 30

calculate_variance_covariance_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days)
