import yfinance as yf

Company = input("Enter in a Ticker: ")

Ticker = yf.Ticker(Company)

#print(Ticker.info.keys())

# Company Sector
print(Ticker.info['sector'], Ticker.info['trailingPE'], Ticker.info['beta'])

