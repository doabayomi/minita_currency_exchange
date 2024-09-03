#!/usr/bin/python3
import requests
import json


def get_list():
    currency_list_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                        "currency-api@latest/v1/currencies.json"
    response = requests.get(currency_list_url)

    """Try the other URL if first URL is not working"""
    if (response.status_code != 200):
        currencies_list_url = "https://latest.currency-api.pages.dev/" \
                          "v1/currencies.json"
        response = requests.get(currencies_list_url)

    return json.loads(response.json())


def get_latest_prices():
    currency_price_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                         "currency-api@latest/v1/currencies/eur.json"
    response = requests.get(currency_price_url)

    """Try the other URL if first URL is not working"""
    if (response.status_code != 200):
        currencies_list_url = "https://latest.currency-api.pages.dev/" \
                              "v1/currencies/eur.json"
        response = requests.get(currencies_list_url)

    return json.loads(response.json())


def get_prices_at(date):
    pass
