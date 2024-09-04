#!/usr/bin/python3
import requests


def get_currency_list():
    """Gets the list of currencies from currency api

    Returns:
        JSON from api containing currency code and full name
    """
    currency_list_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                        "currency-api@latest/v1/currencies.json"
    response = requests.get(currency_list_url)

    """Try the other URL if first URL is not working"""
    if (response.status_code != 200):
        currencies_list_url = "https://latest.currency-api.pages.dev/" \
                              "v1/currencies.json"
        response = requests.get(currencies_list_url)

    return response.json()


def get_latest_rates():
    """Get the latest prices for each currency based on EUR from
    currency api

    Returns:
        JSON containing code of currency and price.
    """
    currency_price_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                         "currency-api@latest/v1/currencies/eur.json"
    response = requests.get(currency_price_url)

    """Try the other URL if first URL is not working"""
    if (response.status_code != 200):
        currencies_list_url = "https://latest.currency-api.pages.dev/" \
                              "v1/currencies/eur.json"
        response = requests.get(currencies_list_url)

    return response.json()


def convert_currency(currency_from, currency_to, amount):
    pass


def get_prices_at(date):
    pass
