import matplotlib.pyplot as plt
import vectorbt as vbt

# Fetch historical data for ETH
# Note: This requires internet access to fetch data from Yahoo Finance
eth_data = vbt.YFData.download(
    'ETH-USD', 
    start='2023-01-01 UTC', 
    end='2023-12-31 UTC').get('Close')

# Calculate indicators for each strategy
# Moving Average Crossover Strategy
short_ma = vbt.MA.run(eth_data, window=10)
long_ma = vbt.MA.run(eth_data, window=50)

# Generate entries for when short_ma crosses above long_ma
mac_entries = short_ma.ma_crossed_above(long_ma)

# Generate exits for when short_ma crosses below long_ma
mac_exits = short_ma.ma_crossed_below(long_ma)

# RSI Strategy
rsi = vbt.RSI.run(eth_data)
rsi_entry = rsi.rsi_below(30)
rsi_exit = rsi.rsi_above(70)

# Bollinger Bands Strategy
bb = vbt.BBANDS.run(eth_data)
bb_entry = eth_data < bb.lower
bb_exit = eth_data > bb.upper

# Combine signals
entries = mac_entries | rsi_entry | bb_entry
exits = mac_exits | rsi_exit | bb_exit

# Backtest Strategies
portfolio = vbt.Portfolio.from_signals(eth_data, entries, exits, fees=0.001, freq='1D')

eth_data.plot(figsize=(14, 7), title='ETH Price with Buy and Sell Signals')

# Overlay the MACD entry and exit signals
plt.scatter(eth_data.index[mac_entries], eth_data[mac_entries], color='green', label='MACD Buy Signal', marker='^', alpha=1)
plt.scatter(eth_data.index[mac_exits], eth_data[mac_exits], color='green', label='MACD Sell Signal', marker='v', alpha=1)

# Overlay the RSI entry and exit signals
plt.scatter(eth_data.index[rsi_entry], eth_data[rsi_entry], color='blue', label='RSI Buy Signal', marker='^', alpha=1)
plt.scatter(eth_data.index[rsi_exit], eth_data[rsi_exit], color='blue', label='RSI Sell Signal', marker='v', alpha=1)

# Overlay the Bollinger Bands entry and exit signals
plt.scatter(eth_data.index[bb_entry], eth_data[bb_entry], color='orange', label='BB Buy Signal', marker='^', alpha=1)
plt.scatter(eth_data.index[bb_exit], eth_data[bb_exit], color='orange', label='BB Sell Signal', marker='v', alpha=1)

# Show the legend
plt.legend()

# Enhance plot readability
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust the layout to make room for the rotated x-axis labels

# Show the plot
plt.show()

# Plot cumulative returns
portfolio.cumulative_returns().plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()