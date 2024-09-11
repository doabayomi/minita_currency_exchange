#!/usr/bin/python3
from market import get_news_for_currencies
from config import Config

output = get_news_for_currencies('USD',
                                 'EUR',
                                 Config.MARKET_AUX_API_KEY)
print(output)
