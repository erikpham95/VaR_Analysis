import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_monte_carlo_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days, simulations_count):
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
    mean_return = np.mean(portfolio_returns)
    std_return = np.std(portfolio_returns)

    # Monte Carlo simulation
    simulated_returns = np.random.normal(loc=mean_return, scale=std_return, size=(simulations_count, time_period_days))
    simulated_portfolio_values = np.prod(1 + simulated_returns, axis=1) - 1

    # Calculate VaR at the specified confidence level
    VaR = -np.percentile(simulated_portfolio_values, 100 - (confidence_interval * 100))

    print(f"Value at Risk (VaR) at {confidence_interval * 100}% confidence level over {time_period_days} days is {VaR * 100:.2f}%")

    # Plotting the distribution of simulated portfolio returns
    plt.hist(simulated_portfolio_values * 100, bins=50, density=True, label="Portfolio Returns")
    plt.axvline(-VaR * 100, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval * 100:.0f}% confidence level')
    plt.xlabel(f'{time_period_days}-Day Portfolio Return (Percentage)')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Simulated Portfolio {time_period_days}-Day Returns (Percentage) - Monte Carlo Method')
    plt.legend()
    plt.show()

# Example usage
tickers = ['XLK', 'XLC', 'XLY', 'XLE', 'XLI', 'XLB', 'XLF', 'XLRE', 'XLP', 'XLU', 'XLV', 'FXI', 'GDX']
weights = [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.13, 0.1]
start_date = '2018-08-10'
end_date = '2023-08-10'
confidence_interval = 0.95
time_period_days = 30
simulations_count=10000

calculate_monte_carlo_var(tickers, weights, start_date, end_date, confidence_interval, time_period_days, simulations_count)
