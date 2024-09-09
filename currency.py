#!/usr/bin/python3
import requests
from datetime import date, timedelta
from flask import url_for
import json


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


def convert_currency_at(currency_from, currency_to, amount, target_date):
    """Converts an amount from one currency to another

    Args:
        currency_from: Currency to convert from
        currency_to: Currency to convert to
        amount: Amount to be converted in initial currency

    Returns:
        (float) Amount in target currency (currency_to)
    """
    current_rates = get_rates_at(target_date)
    currency_from_rate = float(current_rates['eur'][currency_from])
    currency_to_rate = float(current_rates['eur'][currency_to])

    """We convert it first to base currency (EUR) and then
    the target currency we want
    """
    amount_in_euros = float(amount) / currency_from_rate
    amount_in_target_currency = amount_in_euros * currency_to_rate

    """Since its money we step down to 2 decimal places"""
    return round(amount_in_target_currency, 2)


def get_relative_rates_for(currency_from, currency_to, no_of_days):
    """Finds relative rates for currencies in calculation

    Args:
        currency_from: Currency converted from previously
        currency_to: Currency converted to previously
        no_of_days: no of days to find rates for

    Returns:
        (dict) A dictionary of date and their corresponding relative rates
    """
    start_date = date.today() - timedelta(days=no_of_days)
    data = {}

    date_in_session = start_date
    for i in range(no_of_days):
        relative_rate = convert_currency_at(currency_from, currency_to,
                                            1, date_in_session)
        data[date_in_session.isoformat()] = relative_rate
        date_in_session += timedelta(days=1)

    return data


def get_week_currency_data(currency_from, currency_to):
    to_hist_with_usd = get_relative_rates_for(currency_from, 'usd', 7)
    from_hist_with_usd = get_relative_rates_for(currency_from, 'usd', 7)
    relative_history = get_relative_rates_for(currency_from, currency_to, 7)

    price_data = {}
    price_data['dates'] = list(relative_history.keys())
    price_data['base_currency_prices'] = list()
    price_data['target_currency_prices'] = list()
    price_data['relative_currency_prices'] = list()

    for date in price_data["dates"]:
        price_data['base_currency_prices'].append(from_hist_with_usd[date])
        price_data["target_currency_prices"].append(to_hist_with_usd[date])
        price_data["relative_currency_prices"].append(relative_history[date])

    return price_data


def export_data_to_chart(currency_from, currency_to, file_path):
    price_data = get_week_currency_data(currency_from, currency_to)
    data_file = open(file_path, 'w')
    data_file.write(json.dumps(price_data))
    data_file.close()
