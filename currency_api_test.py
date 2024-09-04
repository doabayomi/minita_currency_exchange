#!/usr/bin/python3
"""Test Script for Currency Price APIs"""
import requests

currency_list_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/" \
                    "currency-api@latest/v1/currencies/eur.json"
response = requests.get(currency_list_url)
if (response.status_code != 200):
    currencies_list_url = "https://latest.currency-api.pages.dev/" \
                          "v1/eur.json"
    response = requests.get(currencies_list_url)

data = response.json()
print(data['eur']['aed'])
