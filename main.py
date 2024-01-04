"""
main.py
"""

import json
import os
import time

import requests


def send_discord_notification(title, description, color=0x00FF00):
    """
    Send a styled message to a Discord channel using webhooks.
    :param title: Title of the embed
    :param description: Description or content of the message
    :param color: Color of the embed, in hexadecimal (default green)
    :return:
    """
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url is None:
        print("Error: DISCORD_WEBHOOK_URL is not set.")
        return

    # Create an embed
    embed = {"title": title, "description": description, "color": color}

    # Prepare the payload
    data = {"embeds": [embed]}

    # Send the request
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()


def compare_and_notify(current_symbols, new_symbols, exchange_name):
    """
    Compare current symbols and new symbols, send notification if changed
    :param current_symbols: symbols from local file
    :param new_symbols: symbols from api
    :param exchange_name: exchange name
    :return:
    """
    if current_symbols != new_symbols:
        change_type = (
            "[REMOVED]" if len(current_symbols) > len(new_symbols) else "✅[LISTED]"
        )
        diff_symbols = list(
            current_symbols - new_symbols
            if change_type == "❌[REMOVED]"
            else new_symbols - current_symbols
        )
        diff_symbols_str = ", ".join(diff_symbols)
        title = f"{exchange_name} Futures Symbol Update"
        description = f"{change_type} Symbols: {diff_symbols_str}"
        color = 0xFF0000 if change_type == "❌[REMOVED]" else 0x00FF00

        send_discord_notification(title, description, color)


if __name__ == "__main__":
    from crypto_listed_detector.detector import Detector

    detector = Detector()
    symbols_file = "symbols.json"

    while True:
        if not os.path.exists(symbols_file):
            detector.output_all_exchange_symbols()
        else:
            print("symbols.json already exists.")

        all_symbols = json.load(open(symbols_file))

        new_all_symbols = detector.get_all_exchange_symbols()

        for exchange in all_symbols.keys():
            current_symbols = set(all_symbols[exchange])
            new_symbols = set(new_all_symbols[exchange])
            compare_and_notify(current_symbols, new_symbols, exchange)

        detector.output_all_exchange_symbols()
        time.sleep(60)
