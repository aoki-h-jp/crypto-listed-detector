"""
mexc api fetcher
"""

import requests


class MexcFetch:
    _BASE_URL = "https://contract.mexc.com"
    def __init__(self):
        pass

    def get_risk_reverse(self):
        url = self._BASE_URL + "/api/v1/contract/risk_reverse"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["symbol"] for item in self.get_risk_reverse()["data"]]
