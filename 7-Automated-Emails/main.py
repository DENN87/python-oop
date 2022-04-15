import requests
from pprint import pprint

class NewsFeed:
    """
    Representing multiple news titles and links as a single string
    """
    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        pass