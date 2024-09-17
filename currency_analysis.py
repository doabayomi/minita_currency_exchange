from currency_api import get_relative_rates_for
import numpy as np


def calculate_volatility(base_currency, target_currency, time_period):
    """Calculates the volatility period for a given number of days

    Args:
        base_currency: Currency coverted/compared from
        target_currency: Currency converted/compared to
        time_period: Time period in days

    Returns:
        Volatility index of time period in days
    """
    data = get_relative_rates_for(base_currency, target_currency,
                                  time_period)
    prices = list(data.values())
    daily_returns = []

    for i in range(1, len(prices)):
        daily_return = (prices[i] - prices[i - 1]) / prices[i - 1]
        daily_returns.append(daily_return)

    volatility = np.std(daily_returns)
    return volatility
