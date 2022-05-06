import yfinance as yf

Company = input("Enter in a Ticker: ")
#Company.upper()
Ticker = yf.Ticker(Company)

#print(Ticker.info.keys())

print('\nCompany Information')
print('-------------------')
print('Company Sector: ',Ticker.info['sector'])
print('Market CAP: ',Ticker.info['marketCap'])

print('\nPrice Changes')
print('---------------')
print('Market Open Price: ',Ticker.info['regularMarketOpen'])
print('Previous Close Price: ',Ticker.info['previousClose'])
print('52 Week Change in Price: ',Ticker.info['52WeekChange'])
print('Target Low Price: ',Ticker.info['targetLowPrice'])
print('Target Median Price: ',Ticker.info['targetMedianPrice'])
print('Target High Price: ',Ticker.info['targetHighPrice'])

print('\nPerformance Outlook')
print('---------------------')
print('Ebitda: ',Ticker.info['ebitda'])
print('Ebitda Margins: ',Ticker.info['ebitdaMargins'])
print('3-Year Beta: ',Ticker.info['beta3Year'])
print('Current Beta: ',Ticker.info['beta'])
print('Short Ratio: ',Ticker.info['shortRatio'])

beta = Ticker.info['beta']
print('PEG Ratio: ',Ticker.info['pegRatio'])
print('YTD Return: ',Ticker.info['ytdReturn'])
print('Forward P/E: ',Ticker.info['forwardPE'])
print('Trailing P/E: ',Ticker.info['trailingPE'])

print('\nLong-Term Solvency Ratios')
print('---------------------------')
print('Debt to Equity: ',Ticker.info['debtToEquity'])
d2e= Ticker.info['debtToEquity']
print('PEG Ratio: ',Ticker.info['pegRatio'])
peg= Ticker.info['pegRatio']

print('\nShort-Term Solvency Ratios')
print('----------------------------')
print('Current Ratio: ',Ticker.info['currentRatio'])
current = Ticker.info['currentRatio']
print('Quick Ratio: ',Ticker.info['quickRatio'])
quick = Ticker.info['quickRatio']
