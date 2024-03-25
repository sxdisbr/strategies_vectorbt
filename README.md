# Ethereum Trading Strategies Analysis

This project explores several trading strategies for Ethereum (ETH) using historical price data, with the aim of identifying profitable entry and exit points. The strategies analyzed include Moving Average Crossover, Relative Strength Index (RSI), and Bollinger Bands, utilizing the `vectorbt` Python library for backtesting.

## Getting Started

### Prerequisites

Before running this analysis, ensure you have Python installed on your system along with the following libraries:
- `matplotlib` for plotting the data and signals
- `vectorbt` for fetching historical data, generating signals, and backtesting strategies

You can install these libraries using pip:

```bash
pip install matplotlib vectorbt
```

## Running the Analysis

The main script (strategies_vectorbt.py) performs the following steps:

    Fetches historical ETH data from Yahoo Finance.
    Calculates indicators for each of the three strategies.
    Generates entry and exit signals based on these indicators.
    Backtests these strategies to visualize performance and potential profitability.

To run the analysis, simply execute:

```bash
python strategies_vectorbt.py
```

## Strategies Overview

### Moving Average Crossover

This strategy generates buy signals when a short-term moving average crosses above a long-term moving average, and sell signals when it crosses below.

### RSI (Relative Strength Index)

The RSI strategy identifies overbought and oversold conditions. Buy signals are generated when the RSI is below 30 (oversold), and sell signals are generated when the RSI is above 70 (overbought).

### Bollinger Bands

Buy signals are generated when the price hits the lower Bollinger Band (indicating potential oversold conditions), and sell signals are generated when the price hits the upper Bollinger Band (indicating potential overbought conditions).

## Visualization

The script plots the ETH price data along with buy and sell signals for each strategy. It also plots the cumulative returns of the combined strategy to assess its performance over time.

## Results

The effectiveness of each strategy varies based on market conditions. This analysis provides a foundation for further exploration and optimization of trading strategies for Ethereum.

## Disclaimer

This analysis is for educational purposes only and not financial advice. Always conduct your own research before making any investment decisions.

## License

This project is licensed under the MIT License.
