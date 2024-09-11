#!/usr/bin/python3
import currency
rates = currency.get_relative_rates_for('aed', 'usd', 7)
print(rates)
