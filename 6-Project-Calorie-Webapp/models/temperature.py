import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents a temperature value extracted from the
    timeanddate.com/weather page
    """
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    base_url = 'http://www.timeanddate.com/weather/'
    yml_path = 'models/temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string by adding the country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns a dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, self.headers)
        full_response = r.text
        raw_response = extractor.extract(full_response)
        return raw_response

    def get(self):
        """Gets temp data from response"""
        scraped_content = self._scrape()
        f_to_c = round((float(scraped_content['temp'].replace("°F", "").strip()) - 32) / 1.8)
        return f_to_c

#
# if __name__ == "__main__":
#     temp = Temperature("usa", "san francisco").get()
#     print(temp)
