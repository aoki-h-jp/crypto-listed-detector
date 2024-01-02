"""
pionex api fetcher
"""

import requests


class PionexFetch:
    _BASE_URL = "https://api.pionex.com"

    def __init__(self):
        pass

    def get_linear_symbols(self):
        url = self._BASE_URL + "/api/v1/common/symbols"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_symbols()["data"]["symbols"]]
