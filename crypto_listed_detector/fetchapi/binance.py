"""
binance api fetcher
"""

import requests


class BinanceFetch:
    _BASE_URL = "https://fapi.binance.com"

    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/fapi/v1/exchangeInfo"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_ticker()["symbols"]]
