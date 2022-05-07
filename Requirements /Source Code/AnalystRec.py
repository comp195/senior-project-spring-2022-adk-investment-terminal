import TickerScrape
# show analysts recommendations

print('\nAnalyst Recommendations')
print('-----------------------')
tick = TickerScrape.Ticker

# show analysts recommendations
print(tick.recommendations)

print('\nMajor Holders')
print('-------------')
# show major holders
print(tick.major_holders)

print('\nInstitutional Holders')
print('---------------------')
# show institutional holders
print(tick.institutional_holders)


