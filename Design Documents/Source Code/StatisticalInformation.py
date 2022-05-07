import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import yfinance as yf


class Stats:

    def read_lines(self):
        len_of_articles_list = []
        file1 = open('data.txt', 'r')
        lines = file1.readlines()
        count = 0
        for line in lines:
            count +=1
            len_of_articles_list.append(line.strip())
        values = [int(i) for i in len_of_articles_list]
        return values

    def show_histogram(self, data):
        a = np.array(data)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist(a, bins='auto')
        plt.title("SENTIMENT")
        plt.show()
        # print(sentiment.get_analysis_polarity())

    def pie_chart(self, data):
        Sentiment = ["Positive", "Negative", "Neutral"]
        fig = plt.figure(figsize=(10, 7))
        plt.pie(data, labels=Sentiment, autopct='%1.1f%%', shadow=True, startangle=90)

        # show plot
        plt.show()

#     def time_series(self):
#        # enter_ticker = self.lineEdit.text()
#         price_history = yf.Ticker('UCTT').history(period='2y',
#                                                         # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#                                                         interval='1wk',
#                                                         # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#                                                         actions=False)
#         time_series = list(price_history['Open'])
#         df = pd.read_csv(,
#                          parse_dates=True,
#                          index_col="Date")
#
#         # displaying the first five rows of dataset
#         df.head()
#
#         df['Volume'].plot()
#
#         df.plot(subplots=True, figsize=(10, 12))
#         df.show()
#
# s = Stats()
#
# s.time_series()


