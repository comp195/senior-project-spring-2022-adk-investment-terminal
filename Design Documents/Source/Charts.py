import TickerScrape
import yfinance as yf

msft = TickerScrape.Ticker

# get stock info
#print(msft.info)

# get historical market data
#hist = msft.history(period="max")


# show financials
#print(msft.financials)
#print(msft.quarterly_financials)


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


# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

