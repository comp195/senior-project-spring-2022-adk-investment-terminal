from nltk.sentiment import SentimentIntensityAnalyzer
from newspaper import Config
from newspaper import Article
from textblob import TextBlob
import newspaper
import nltk

import Google_News_Scrapper


# nltk.download('vader_lexicon')
# nltk.download('punkt')

# company_articles = Google_News_Scrapper.ScrapeArticles()


class SentimentAnalysis():

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


# Takes some time to parse and compute the sentiment. will work on improving the speed
# you can change the arguments below                   'ticker' Start_date    End_date
company_articles = Google_News_Scrapper.ScrapeArticles('NVDA', '08/01/2021', '8/07/2021')
sentiment = SentimentAnalysis()
sentiment.lexical_article_analyze(company_articles.search_articles()[0][0:5])

# print('______________________________________________________________________________________________________')
#
# for i in range(len(sentiment.summary)):
#     print(sentiment.summary[i])
#     print('______________________________________________________________________________________________________')
