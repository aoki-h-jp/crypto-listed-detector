"""
main.py
"""
import json
import os
import requests


def send_discord_notification(message):
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    if webhook_url is None:
        print("エラー: DISCORD_WEBHOOK_URLが設定されていません。")
    data = {'content': message}
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()


# TODO: logging
# TODO: pytest
if __name__ == "__main__":
    from crypto_listed_detector.detector import Detector

    detector = Detector()

    if not os.path.exists("symbols.json"):
        detector.output_all_exchange_symbols()
    else:
        send_discord_notification("symbols.json already exists.")

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
        send_discord_notification("bybit symbols are the same")
    else:
        send_discord_notification("bybit symbols are different")
        send_discord_notification("new symbols:")
        send_discord_notification(new_bybit_symbols - bybit_symbols)

    if mexc_symbols == new_mexc_symbols:
        send_discord_notification("mexc symbols are the same")
    else:
        send_discord_notification("mexc symbols are different")
        send_discord_notification("new symbols:")
        send_discord_notification(new_mexc_symbols - mexc_symbols)

    if gateio_symbols == new_gateio_symbols:
        send_discord_notification("gateio symbols are the same")
    else:
        send_discord_notification("gateio symbols are different")
        send_discord_notification("new symbols:")
        send_discord_notification(new_gateio_symbols - gateio_symbols)
