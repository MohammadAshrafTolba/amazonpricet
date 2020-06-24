from selectorlib import Extractor
import requests
from config import basedir


class AmazonCrawler():

    def __init__(self, URL):
        # create an Extractor by reading from YAML file
        extractor = Extractor.from_yaml_file(basedir + '/app/crawler/selectors.yml')
        headers = {
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.amazon.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = requests.get(URL, headers=headers)
        self.product_data = extractor.extract(response.text)

    def get_price(self):
        price = self.product_data['price1'] or self.product_data['price2'] \
                or self.product_data['price3'] or self.product_data['price4'] or self.product_data['price5']
        if price is not None:
            return float(price[1:])
        return None

    def get_title(self):
        product_title = self.product_data['name']
        return product_title

    def get_product_data(self):
        price = self.get_price()
        product_title = self.get_title()
        return price, product_title