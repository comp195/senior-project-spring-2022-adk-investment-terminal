import matplotlib.pyplot as plt
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from newspaper import Config
from newspaper import Article
from textblob import TextBlob
import newspaper
import nltk

import Google_News_Scrapper
from StatisticalInformation import Stats

from datetime import date

# nltk.download('vader_lexicon')
# nltk.download('punkt')

# company_articles = Google_News_Scrapper.ScrapeArticles()
stats_clss = Stats()


class SentimentAnalysis:

    def __init__(self):
        self.positive_sentiment_list = []
        self.neutral_sentiment_list = []
        self.negative_sentiment_list = []
        self.analysis_polarity = []
        self.summary = []
        self.positive_counter = 0
        self.neutral_counter = 0
        self.negative_counter = 0
        self.sum_total_polarity = 0

    @classmethod
    def parse_articles(cls, articles):
        article = Article(articles, fetch_images=False)
        article.download()
        try:
            article.parse()
            article.nlp()
        except Exception as e:
            print(e)
        return article

    def analyze_sentence(self, article):
        analysis = TextBlob(article.text)
        self.analysis_polarity.append(analysis.polarity)
        return analysis

    def lexical_article_analyze(self, loop):

        print('7')

        for articles in loop:
            parsed_article = self.parse_articles(articles)
            analysis = self.analyze_sentence(parsed_article)
            self.sum_total_polarity += analysis.polarity
            self.summary.append(parsed_article.summary)

            for sentence in analysis.sentences:
                if sentence.polarity > 0:
                    self.positive_counter += 1
                    self.positive_sentiment_list.append(sentence)
                elif sentence.polarity < 0:
                    self.neutral_counter += 1
                    self.negative_sentiment_list.append(sentence)
                else:
                    self.neutral_counter += 1
                    self.neutral_sentiment_list.append(sentence)

    def basic_stats(self):
        total_reviewed_sentences = (self.positive_counter + self.neutral_counter + self.negative_counter)
        print(total_reviewed_sentences)

    def show_histogram(self):
        a = self.analysis_polarity
        stats_clss.show_histogram(a)

    def histogram(self):
        a = np.array(self.analysis_polarity)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist(a, bins='auto')
        plt.title("SENTIMENT")
        plt.show()

    def pie_chart(self):
        data = [len(self.positive_sentiment_list), len(self.negative_sentiment_list), len(self.neutral_sentiment_list)]
        stats_clss.pie_chart(data)

    def store_sentiment_data(self):
        data = [len(self.positive_sentiment_list), len(self.negative_sentiment_list), len(self.neutral_sentiment_list)]
        with open('data.txt', 'w') as f:
            for item in data:
                f.write("%d\n" % item)

# Takes some time to parse and compute the sentiment. will work on improving the speed
# you can change the arguments below                   'ticker' Start_date    End_date
###########################################################################################
# today = date.today()
# print("Today's date:", today)
# company_articles = Google_News_Scrapper.ScrapeArticles('NVDA', '04/05/2022', today)
# sentiment = SentimentAnalysis()
# sentiment.lexical_article_analyze(company_articles.search_articles()[0][0:5])
#
# sentiment.store_sentiment_data()
#####################################################################################
# sentiment.show_histogram()
# sentiment.pie_chart()
# sentiment.basic_stats()
# sentiment.histogram()
# sentiment.pie_chart()
# print('______________________________________________________________________________________________________')
#
# for i in range(len(sentiment.summary)):
#     print(sentiment.summary[i])
#     print('______________________________________________________________________________________________________')
