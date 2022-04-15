import requests
from pprint import pprint

class NewsFeed:
    """
    Representing multiple news titles and links as a single string
    """

    base_url = "http://newsapi.org/v2/everything"
    api_key = "890603a55bfa47048e4490069ebee18c"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}?qInTitle={self.interest}" \
              f"&from={self.from_date}&to={self.to_date}" \
              f"&language={self.language}&apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


news_feed = NewsFeed('tesla', '2022-03-14', '2022-04-14', 'en')
print(news_feed.get())
