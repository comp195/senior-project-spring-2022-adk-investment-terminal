import TickerScrape
# show analysts recommendations

print('\nCompany Actions')
print('----------------')
tick = TickerScrape.Ticker
# show actions (dividends, splits)
print(tick.actions)

print('\nDividends')
print('----------')
# show dividends
print(tick.dividends)

print('\nSplits')
print('-------')
# show splits
print(tick.splits)

print('\nISIN Code - International Securities Identification Number')
print('-----------------------------------------------------------')
# show isin
print(tick.isin)

print('\nOptions Expirations')
print('--------------------')
# show options expirations
print(tick.options)