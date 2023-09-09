import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_historical_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days):
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

    # Finding X-Day Historical Returns
    range_returns = portfolio_returns.rolling(window=time_period_days).sum().dropna()

    # Calculating VaR using the Historical Method
    VaR = -np.percentile(range_returns, 100 - (confidence_interval * 100))

    print(f"Value at Risk (VaR) at {confidence_interval * 100}% confidence level over {time_period_days} days is {VaR * 100:.2f}%")

    # Plotting the Results of the Historical Returns
    plt.hist(range_returns * 100, bins=50, density=True, label="Portfolio Returns")
    plt.axvline(-VaR * 100, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval * 100:.0f}% confidence level')
    plt.xlabel(f'{time_period_days}-Day Portfolio Return (Percentage)')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Portfolio {time_period_days}-Day Returns (Percentage) - Historical Method')
    plt.legend()
    plt.show()

# Example usage
tickers = ['XLK', 'XLC', 'XLY', 'XLE', 'XLI', 'XLB', 'XLF', 'XLRE', 'XLP', 'XLU', 'XLV', 'FXI', 'GDX']
weights = [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.13, 0.1]
start_date = '2018-08-10'
end_date = '2023-08-10'
confidence_interval = 0.95
time_period_days = 30

calculate_historical_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days)
