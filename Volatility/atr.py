import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def atr(data, window=14):
	high_low = data['High'] - data['Low']
	high_close = (data['High'] - data['Close'].shift()).abs()
	low_close = (data['Low'] - data['Close'].shift()).abs()

	ranges = pd.concat([high_low, high_close, low_close], axis=1)
	true_range = ranges.max(axis=1)

	atr = true_range.rolling(window=window).mean()

	return atr


def plot_atr(data):
	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8), sharex=True)

	ax1.plot(data.index, data['Close'], linewidth=1.5, color='black', label='Close Price')
	ax1.set_title('Price Chart')
	ax1.set_ylabel('Price')
	ax1.legend()

	ax2.plot(data.index, data['atr'], linewidth=1.5, color='blue', label='ATR')
	ax2.set_title('Average True Range (ATR)')
	ax2.set_ylabel('ATR')
	ax2.set_xlabel('Date')
	ax2.legend()

	plt.show()


data = pd.read_csv('../BTCUSDT.csv')

atr = atr(data)

data['atr'] = atr

plot_atr(data)