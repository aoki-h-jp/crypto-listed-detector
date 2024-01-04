"""
okx api fetcher
"""

import requests


class OkxFetch:
    _BASE_URL = "https://www.okx.com"

    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/api/v5/public/instruments?instType=SWAP"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["instId"] for item in self.get_linear_ticker()["data"]]
