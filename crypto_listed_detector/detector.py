"""
crypto-listed-detector
"""
import json

from crypto_listed_detector.fetchapi.binance import BinanceFetch
from crypto_listed_detector.fetchapi.bitget import BitgetFetch
from crypto_listed_detector.fetchapi.bybit import BybitFetch
from crypto_listed_detector.fetchapi.gateio import GateioFetch
from crypto_listed_detector.fetchapi.kucoin import KucoinFetch
from crypto_listed_detector.fetchapi.mexc import MexcFetch
from crypto_listed_detector.fetchapi.phemex import PhemexFetch
from crypto_listed_detector.fetchapi.pionex import PionexFetch
from crypto_listed_detector.fetchapi.xtcom import XtcomFetch


class Detector:
    def __init__(self):
        """
        Init all fetchers
        """
        self.bybit = BybitFetch()
        self.gateio = GateioFetch()
        self.mexc = MexcFetch()
        self.bitget = BitgetFetch()
        self.xtcom = XtcomFetch()
        self.pionex = PionexFetch()
        self.phemex = PhemexFetch()
        self.binance = BinanceFetch()
        self.kucoin = KucoinFetch()

    def get_all_exchange_symbols(self):
        """
        Get all symbols from all exchanges
        :return:
        """
        return {
            "bybit": self.bybit.get_all_linear_symbols(),
            "gateio": self.gateio.get_all_linear_symbols(),
            "mexc": self.mexc.get_all_linear_symbols(),
            "bitget": self.bitget.get_all_linear_symbols(),
            "xtcom": self.xtcom.get_all_linear_symbols(),
            "pionex": self.pionex.get_all_linear_symbols(),
            "phemex": self.phemex.get_all_linear_symbols(),
            "binance": self.binance.get_all_linear_symbols(),
            "kucoin": self.kucoin.get_all_linear_symbols(),
        }

    def output_all_exchange_symbols(self):
        """
        Output all symbols to symbols.json
        :return:
        """
        d = self.get_all_exchange_symbols()
        with open("symbols.json", "w") as f:
            json.dump(d, f, indent=4)
