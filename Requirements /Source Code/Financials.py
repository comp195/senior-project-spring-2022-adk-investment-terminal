import TickerScrape
# show Financials
tick = TickerScrape.Ticker

print('\nCompany Financials')
print('-------------------')
print(tick.financials)
print('\nQuarterly Financials')
print('---------------------')
print(tick.quarterly_financials)

print('\nBalance Sheet')
print('--------------')
# Balance Sheet
print(tick.balance_sheet)
print('\nQuarterly Balance Sheet')
print('------------------------')
# Quarterly Balance Sheet
print(tick.quarterly_balance_sheet)

print('\nCashflows')
print('----------')
# Cashflows
print(tick.cashflow)
print('\nQuarterly Cashflows')
print('--------------------')
# Quarterly Cashflows
print(tick.quarterly_cashflow)

print('\nEarnings')
print('---------')
# Earnings
print(tick.earnings)
print('\nQuarterly Earnings')
print('--------------------')
# Quarterly Earnings
print(tick.quarterly_earnings)

print('\nSustainability')
print('---------------')
# Sustainability
print(tick.sustainability)