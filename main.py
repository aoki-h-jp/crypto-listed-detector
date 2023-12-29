"""
main.py
"""
import json
import os

# TODO: logging
if __name__ == "__main__":
    from crypto_listed_detector.detector import Detector

    detector = Detector()

    if not os.path.exists("symbols.json"):
        detector.output_all_exchange_symbols()
    else:
        print("symbols.json already exists.")

    all_symbols = json.load(open("symbols.json"))

    # compare symbols
    bybit_symbols = set(all_symbols["bybit"])
    mexc_symbols = set(all_symbols["mexc"])
    gateio_symbols = set(all_symbols["gateio"])

    new_all_symbols = detector.get_all_exchange_symbols()

    new_bybit_symbols = set(new_all_symbols["bybit"])
    new_mexc_symbols = set(new_all_symbols["mexc"])
    new_gateio_symbols = set(new_all_symbols["gateio"])

    if bybit_symbols == new_bybit_symbols:
        print("bybit symbols are the same")
    else:
        print("bybit symbols are different")
        print("new symbols:")
        print(new_bybit_symbols - bybit_symbols)

    if mexc_symbols == new_mexc_symbols:
        print("mexc symbols are the same")
    else:
        print("mexc symbols are different")
        print("new symbols:")
        print(new_mexc_symbols - mexc_symbols)

    if gateio_symbols == new_gateio_symbols:
        print("gateio symbols are the same")
    else:
        print("gateio symbols are different")
        print("new symbols:")
        print(new_gateio_symbols - gateio_symbols)
