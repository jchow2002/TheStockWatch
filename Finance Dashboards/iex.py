import requests
import config


class IEXStock:

    def __init__(self, token, symbol):
        self.BASE_URL = 'https://cloud.iexapis.com/stable'

        self.token = token
        self.symbol = symbol

    def get_logo(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/logo?token={self.token}"
        r = requests.get(url)
        return r.json()

    def get_company_info(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/company?token={self.token}"
        r = requests.get(url)
        return r.json()

    def get_stats(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/stats?token={self.token}"
        r = requests.get(url)
        return r.json()

    def get_news(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/news?token={self.token}"
        r = requests.get(url)
        return r.json()

    def get_quote(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/quote?token={self.token}"
        r = requests.get(url)
        return r.json()

    def get_chart(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/chart/1m?token={self.token}"
        r = requests.get(url)
        return r.json()
