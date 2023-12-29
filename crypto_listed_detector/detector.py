"""
crypto-listed-detector
"""
import json

from crypto_listed_detector.fetchapi.bybit import BybitFetch
from crypto_listed_detector.fetchapi.gateio import GateioFetch
from crypto_listed_detector.fetchapi.mexc import MexcFetch


class Detector:
    def __init__(self):
        self.bybit = BybitFetch()
        self.gateio = GateioFetch()
        self.mexc = MexcFetch()

    def get_all_exchange_symbols(self):
        return {
            "bybit": self.bybit.get_all_linear_symbols(),
            "gateio": self.gateio.get_all_linear_symbols(),
            "mexc": self.mexc.get_all_linear_symbols()
        }

    def output_all_exchange_symbols(self):
        d = self.get_all_exchange_symbols()
        with open("symbols.json", "w") as f:
            json.dump(d, f)
