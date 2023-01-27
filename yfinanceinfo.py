import yfinance as yf

aapl = yf.Ticker("BA")

print(aapl.info)
