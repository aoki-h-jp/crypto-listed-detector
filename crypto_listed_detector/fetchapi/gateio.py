"""
gateio api fetcher
"""

import requests


class GateioFetch:
    _BASE_URL = "https://api.gateio.ws"

    def __init__(self):
        pass

    def get_contracts(self):
        url = self._BASE_URL + "/api/v4/futures/usdt/contracts"
        response = requests.get(url)
        return response.json()

    def get_all_linear_symbols(self):
        return [item["name"] for item in self.get_contracts()]
