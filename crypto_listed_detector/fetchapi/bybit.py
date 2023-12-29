"""
bybit api fetcher
"""

import requests


class BybitFetch:
    _BASE_URL = "https://api.bybit.com"
    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/v5/market/tickers?category=linear"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_ticker()["result"]["list"]]
