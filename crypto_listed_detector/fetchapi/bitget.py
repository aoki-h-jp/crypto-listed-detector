"""
bitget api fetcher
"""

import requests


class BitgetFetch:
    _BASE_URL = "https://api.bitget.com"

    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/api/v2/mix/market/tickers?productType=USDT-FUTURES"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_ticker()["data"]]
