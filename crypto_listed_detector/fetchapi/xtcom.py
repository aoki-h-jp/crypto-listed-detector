"""
xtcom api fetcher
"""

import requests


class XtcomFetch:
    _BASE_URL = "https://fapi.xt.com"

    def __init__(self):
        pass

    def get_linear_ticker(self):
        url = self._BASE_URL + "/future/market/v1/public/cg/contracts"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_linear_ticker()]
