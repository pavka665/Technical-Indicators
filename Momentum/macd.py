import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    macd_hist = macd_line - signal_line

    return macd_line, signal_line, macd_hist


def plot_macd(data):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    ax1.plot(data.index, data['Close'], color='black', linewidth=1.5)
    ax1.set_title('Price Chart')
    ax1.set_ylabel('Price')

    ax2.plot(data.index, data['macd'], label='MACD', color='blue', linewidth=1)
    ax2.plot(data.index, data['signal'], label='Signal', color='green', linewidth=1)
    ax2.bar(data.index, data['hist'], label='MACD Hist', color='grey')
    ax2.set_title('MACD')
    ax2.set_ylabel('MACD')
    ax2.legend()
    plt.show()



data = pd.read_csv('../BTCUSDT.csv')

macd, signal, hist = macd(data)
data['macd'] = macd
data['signal'] = signal
data['hist'] = hist

plot_macd(data)
