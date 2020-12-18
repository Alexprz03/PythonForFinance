import yfinance as yf

aapl= yf.Ticker("aapl")
aapl

aapl_historical = aapl.history(start="2020-11-01", end="2020-12-20", interval="1h")
print(aapl_historical)

#data = yf.download("AMZN AAPL GOOG", start="2017-01-01",end="2017-04-30", group_by='tickers')
#print(data)


#print(aapl.info['forwardPE'])
