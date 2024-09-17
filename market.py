#!/usr/bin/python3
import requests
"""Market News and Analysis API helper functions"""


def get_news_for_currencies(currency_from, currency_to, api_token):
    """Retrieves relevant news to currencies from MarketAux api from
    the past two weeks.

    Args:
        currency_from: Currency converted from
        currency_to: Currency converted to
        api_token: Secret api token from marketaux

    Returns:
        A JSON of the relevant news gotten.
    """
    params = {
        "symbols": currency_from.upper() + "," + currency_to.upper(),
        "filter_entities": "true",
        "language": "en",
        "api_token": api_token,
    }

    response = requests.get("https://api.marketaux.com/v1/news/all",
                            params=params)
    if response.status_code == 200:
        return response.json()
