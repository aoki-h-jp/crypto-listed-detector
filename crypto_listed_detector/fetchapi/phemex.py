"""
phemex api fetcher
"""

import requests


class PhemexFetch:
    _BASE_URL = "https://api.phemex.com"

    def __init__(self):
        pass

    def get_linear_products(self):
        url = self._BASE_URL + "/public/products"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_products()["data"]["products"]]
