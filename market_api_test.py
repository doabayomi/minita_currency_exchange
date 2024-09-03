#!/usr/bin/python3
import requests
"""Market sentiment and news api test"""

params = {
    "api_token": "zmatKJcQoBE20fIUPIcevF0jKsHED3StedNx1ILK",
    "symbols": "USD, EUR",
    "language": "en",
    "filter_entities": "true"
}
response = requests.get("https://api.marketaux.com/v1/news/all", params=params)
if response.status_code == 200:
    print(response.json())
