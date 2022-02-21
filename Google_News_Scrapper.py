from GoogleNews import GoogleNews


class Scrape_Articles():

    def __init__(self, ticker, start_date, end_date):
        self.company_ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def set_ticker(self, ticker):
        self.company_ticker = ticker

    def get_ticker(self):
        return self.company_ticker

    def search_articles(self):
        googlenews = GoogleNews()
        googlenews.set_time_range(self.start_date, self.end_date)
        googlenews.set_encode('utf-8')
        googlenews.get_news(self.get_ticker())
        googlenews.search(self.get_ticker())
        links = googlenews.get_links()
        result = googlenews.result()
        googlenews.clear()

        protocol = 'https://'
        urls = [protocol + domain if protocol not in domain else domain for domain in links]
        return urls, result

# To test if the program works
news = Scrape_Articles('NVDA', '08/01/2021', '8/16/2021')
print('URLS for Articles on NVIDA', news.search_articles()[0])
print('Results for Articles on NVIDA', news.search_articles()[1])