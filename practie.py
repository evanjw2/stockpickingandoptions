import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt
#%%
# Function to fetch data from Yahoo Finance
def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Function to add technical indicators
def add_technical_indicators(data):
    # Add a 50-period Simple Moving Average (SMA)
    data['SMA_50'] = ta.sma(data['Close'], length=50)
    
    # Add the Relative Strength Index (RSI) with a 14-period window
    data['RSI'] = ta.rsi(data['Close'], length=14)
    
    # Add the Moving Average Convergence Divergence (MACD)
    macd = ta.macd(data['Close'], fast=12, slow=26, signal=9)
    # Ensure the correct columns are used based on the return from ta.macd
    data['MACD'] = macd.iloc[:, 0]  # MACD line
    data['MACD_signal'] = macd.iloc[:, 1]  # Signal line
    data['MACD_hist'] = macd.iloc[:, 2]  # Histogram
    
    return data

# Example usage:
data = fetch_data("NVDA", "2022-01-01", "2023-01-01")
data = add_technical_indicators(data)
print(data.tail())

def plot_data(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Closing Price')
    plt.plot(data['SMA_50'], label='50-Day SMA', alpha=0.7)
    plt.plot(data['RSI'], label='RSI', alpha=0.4)
    plt.title('NVDA Stock Price')
    plt.legend()
    plt.show()

plot_data(data)

#%%