import pandas as pd 
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def bollinger_bands(data, window=20, num_std_dev=2):
	rolling_mean = data['Close'].rolling(window=window).mean()
	rolling_std = data['Close'].rolling(window=window).std()
	upper_band = rolling_mean + (rolling_std * num_std_dev)
	lower_band = rolling_mean - (rolling_std * num_std_dev)
	return rolling_mean, upper_band, lower_band


def plot_bb(data):
	fig, ax = plt.subplots(figsize=(12,6))

	ax.plot(data.index, data['Close'], linewidth=1.5, color='black', label='Close Price')
	ax.plot(data.index, data['rolling_mean'], linewidth=1, color='blue', label='Middle band')
	ax.plot(data.index, data['upper_band'], linestyle='--', color='red', linewidth=1.5, label='Upper Band')
	ax.plot(data.index, data['lower_band'], linestyle='--', color='green', linewidth=1.5, label='Lower Band')

	ax.fill_between(data.index, data['upper_band'], data['lower_band'], color='grey', alpha=0.3)
	ax.set_title('Bollinger Bands')
	ax.set_xlabel('Date')
	ax.set_ylabel('Price')
	ax.legend()

	plt.show()


data = pd.read_csv('../BTCUSDT.csv')

rolling_mean, upper_band, lower_band = bollinger_bands(data, window=15, num_std_dev=1.5)

data['rolling_mean'] = rolling_mean
data['upper_band'] = upper_band
data['lower_band'] = lower_band

plot_bb(data)