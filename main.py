"""
main.py
"""
import json
import os
import time

import requests


def send_discord_notification(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url is None:
        print("エラー: DISCORD_WEBHOOK_URLが設定されていません。")
    data = {"content": str(message)}
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()


# TODO: logging
# TODO: pytest
if __name__ == "__main__":
    from crypto_listed_detector.detector import Detector

    # TODO: cronとかで工夫したい
    while True:
        detector = Detector()

        if not os.path.exists("symbols.json"):
            detector.output_all_exchange_symbols()
        else:
            print("symbols.json already exists.")

        all_symbols = json.load(open("symbols.json"))

        # compare symbols
        try:
            bybit_symbols = set(all_symbols["bybit"])
            mexc_symbols = set(all_symbols["mexc"])
            gateio_symbols = set(all_symbols["gateio"])
            bitget_symbols = set(all_symbols["bitget"])
        except KeyError:
            detector.output_all_exchange_symbols()
            bybit_symbols = set(all_symbols["bybit"])
            mexc_symbols = set(all_symbols["mexc"])
            gateio_symbols = set(all_symbols["gateio"])
            bitget_symbols = set(all_symbols["bitget"])

        new_all_symbols = detector.get_all_exchange_symbols()

        new_bybit_symbols = set(new_all_symbols["bybit"])
        new_mexc_symbols = set(new_all_symbols["mexc"])
        new_gateio_symbols = set(new_all_symbols["gateio"])
        new_bitget_symbols = set(new_all_symbols["bitget"])

        if bybit_symbols == new_bybit_symbols:
            print("bybit symbols are the same")
        else:
            if len(bybit_symbols) > len(new_bybit_symbols):
                send_discord_notification("bybit symbols are changed")
                send_discord_notification("[REMOVED] symbols:")
                send_discord_notification(bybit_symbols - new_bybit_symbols)
            else:
                send_discord_notification("bybit symbols are changed")
                send_discord_notification("[LISTED] symbols:")
                send_discord_notification(new_bybit_symbols - bybit_symbols)

        if mexc_symbols == new_mexc_symbols:
            print("mexc symbols are the same")
        else:
            if len(mexc_symbols) > len(new_mexc_symbols):
                send_discord_notification("mexc symbols are changed")
                send_discord_notification("[REMOVED] symbols:")
                send_discord_notification(mexc_symbols - new_mexc_symbols)
            else:
                send_discord_notification("mexc symbols are changed")
                send_discord_notification("[LISTED] symbols:")
                send_discord_notification(new_mexc_symbols - mexc_symbols)

        if gateio_symbols == new_gateio_symbols:
            print("gateio symbols are the same")
        else:
            if len(gateio_symbols) > len(new_gateio_symbols):
                send_discord_notification("gateio symbols are changed")
                send_discord_notification("[REMOVED] symbols:")
                send_discord_notification(gateio_symbols - new_gateio_symbols)
            else:
                send_discord_notification("gateio symbols are changed")
                send_discord_notification("[LISTED] symbols:")
                send_discord_notification(new_gateio_symbols - gateio_symbols)

        if bitget_symbols == new_bitget_symbols:
            print("bitget symbols are the same")
        else:
            if len(bitget_symbols) > len(new_bitget_symbols):
                send_discord_notification("bitget symbols are changed")
                send_discord_notification("[REMOVED] symbols:")
                send_discord_notification(bitget_symbols - new_bitget_symbols)
            else:
                send_discord_notification("bitget symbols are changed")
                send_discord_notification("[LISTED] symbols:")
                send_discord_notification(new_bitget_symbols - bitget_symbols)

        send_discord_notification("done")

        time.sleep(60)
