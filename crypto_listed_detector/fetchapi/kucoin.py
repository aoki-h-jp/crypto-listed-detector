"""
kucoin api fetcher
"""

import requests


class KucoinFetch:
    _BASE_URL = "https://api-futures.kucoin.com"

    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/api/v1/contracts/active"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_ticker()["data"]]
