#!/usr/bin/python3
import requests
from datetime import date, timedelta


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


def get_rates_at(target_date: date):
    """Gets exchange rates at a specific date

    Args:
        target_date: Date to find target date

    Returns:
        JSON containing rates for each currency at target date
    """
    if target_date == date.today():
        date_as_string = "latest"
    else:
        date_as_string = date.isoformat(target_date)

    price_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                f"currency-api@{date_as_string}/v1/currencies/eur.json"
    fallback_price_url = f"https://{date_as_string}.currency-api.pages.dev/" \
                         "v1/currencies/eur.json"

    response = requests.get(price_url)
    if response.status_code != 200:
        response = requests.get(fallback_price_url)

    return response.json()


def get_latest_rates():
    """Get the latest prices for each currency based on EUR from
    currency api

    Returns:
        JSON containing code of currency and price.
    """
    latest_rates = get_rates_at(date.today())
    return latest_rates


def convert_currency(currency_from, currency_to, amount):
    """Converts an amount from one currency to another

    Args:
        currency_from: Currency to convert from
        currency_to: Currency to convert to
        amount: Amount to be converted in initial currency

    Returns:
        (float) Amount in target currency (currency_to)
    """
    current_rates = get_latest_rates()
    currency_from_rate = current_rates[currency_from]
    currency_to_rate = current_rates[currency_to]

    """We convert it first to base currency (EUR) and then
    the target currency we want
    """
    amount_in_euros = amount / currency_from_rate
    amount_in_target_currency = amount_in_euros * currency_to_rate

    return amount_in_target_currency
