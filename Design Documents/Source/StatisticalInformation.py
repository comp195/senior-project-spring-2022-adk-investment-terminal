import numpy as np
from matplotlib import pyplot as plt


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
        # data = [len(self.positive_sentiment_list), len(self.negative_sentiment_list), len(self.neutral_sentiment_list)]
        Sentiment = ["Positive", "Negative", "Neutral"]
        fig = plt.figure(figsize=(10, 7))
        plt.pie(data, labels=Sentiment)

        # show plot
        plt.show()
