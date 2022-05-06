import TickerScrape
import yfinance as yf

msft = TickerScrape.Ticker

# get stock info
#print(msft.info)

# get historical market data
#hist = msft.history(period="max")

# show actions (dividends, splits)
#print(msft.actions)

# show dividends
#print(msft.dividends)

# show splits
#print(msft.splits)

# show financials
#print(msft.financials)
#print(msft.quarterly_financials)

# show major holders
#print(msft.major_holders)

# show institutional holders
#print(msft.institutional_holders)

# show balance sheet
#print(msft.balance_sheet)
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
#print(msft.recommendations)

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news
