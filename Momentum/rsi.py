import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def plot_rsi(data):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax1.plot(data.index, data['Close'], color='black', linewidth=1.5)
    ax1.set_title('Price chart')
    ax1.set_ylabel('Price')

    ax2.plot(data.index, data['rsi'], label='RSI', color='blue', linewidth=1)
    ax2.axhline(70, linestyle='--', color='red', linewidth=1.5)
    ax2.axhline(30, linestyle='--', color='green', linewidth=1.5)
    ax2.set_title('RSI')
    ax2.set_ylabel('RSI')
    ax2.legend()

    plt.show()

data = pd.read_csv('../BTCUSDT.csv')
rsi = rsi(data)

data['rsi'] = rsi

plot_rsi(data)

