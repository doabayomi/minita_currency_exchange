from flask import Flask, render_template, request, jsonify
from flask_caching import Cache
from currency_api import (
    get_currency_list,
    get_relative_rates_for,
    convert_currency_at,
    get_yearly_aggregate_data
)
from currency_analysis import calculate_volatility
import market_news_api
from datetime import date
"""Main Flask app for caching, routes and api interaction"""


app = Flask(__name__)

"""Getting API keys"""
app.config.from_object("config.Config")
news_api_token = app.config['MARKET_AUX_API_KEY']

"""Setting up Cache"""
cache = Cache()
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)


@cache.memoize(timeout=36000)
def fetch_currency_list():
    """Cached function for getting currency list

    Returns:
        Currency list
    """
    return get_currency_list()


@cache.memoize(timeout=3600)
def convert_currency(base_currency, target_currency, amount):
    """Cached function for currency conversion

    Args:
        base_currency: Currency converted from
        target_currency: Currency converted to
        amount: Amount being converted

    Returns:
        Converted amount in target currency
    """
    return convert_currency_at(base_currency, target_currency,
                               amount, date.today())


@cache.memoize(timeout=7200)
def get_currency_news(base_currency, target_currency):
    """Cached news function for market news

    Args:
        base_currency: Currency converted from
        target_currency: Currency converted to

    Returns:
        JSON containing currency news for both currencies
    """
    return market_news_api.get_news_for_currencies(base_currency,
                                                   target_currency,
                                                   news_api_token)


@cache.memoize(timeout=64800)
def calculate_volatility_cached(base_currency, target_currency, days):
    return calculate_volatility(base_currency, target_currency, days)


@app.route("/", methods=["GET"])
def index():
    """Home page"""
    currencies = fetch_currency_list()

    amount = request.args.get('amount')
    if amount is None or amount == '':
        """Handle empty or invalid amount"""
        return render_template("index.html", currencies=currencies,
                               input="empty")

    amount = request.args.get('amount')
    currency_from = request.args.get('from')
    currency_to = request.args.get('to')

    converted_amount = convert_currency(currency_from, currency_to,
                                        amount)
    base_rates = {
        'from': round(convert_currency(currency_from, currency_to, 1), 5),
        'to': round(convert_currency(currency_to, currency_from, 1), 5)
    }

    """1 month volatility index"""
    base_volatility = calculate_volatility_cached('usd', currency_from, 30)
    target_volatility = calculate_volatility_cached('usd', currency_to, 30)

    """Preparing results from conversion """
    answer = {
        'amount': round(float(amount), 2),
        'currency_from': currency_from,
        'currency_to': currency_to,
        'converted_amount': round(converted_amount, 2),
        'base_volatility': base_volatility,
        'target_volatility': target_volatility,
        'base_rates': base_rates
        }

    """Getting market news"""
    try:
        news = get_currency_news(currency_from, currency_to)
    except Exception as e:
        news = {'data': [], 'error': 'Failed to fetch news'}

    return render_template("index.html", currencies=currencies,
                           input="valid", result=answer,
                           news=news['data'])


@app.route("/api/prices/weekly/<currency_from>/<currency_to>")
@cache.cached(timeout=64800)
def get_weekly_price_data(currency_from, currency_to):
    """API function for weekly rates data

    Args:
        currency_from: Currency converted from
        currency_to: Currency converted to

    Returns:
        Rates data for past week
    """
    return jsonify(get_relative_rates_for(currency_from, currency_to, 7))


@app.route("/api/prices/monthly/<currency_from>/<currency_to>")
@cache.cached(timeout=64800)
def get_monthly_price_data(currency_from, currency_to):
    """API function for monthly rates data

    Args:
        currency_from: Currency converted from
        currency_to: Currency converted to

    Returns:
        Rates data for past month
    """
    return jsonify(get_relative_rates_for(currency_from, currency_to, 30))


@app.route("/api/prices/quarterly/<currency_from>/<currency_to>")
@cache.cached(timeout=64800)
def get_quarterly_price_data(currency_from, currency_to):
    """API function for quarterly rates data

    Args:
        currency_from: Currency converted from
        currency_to: Currency converted to

    Returns:
        Rates data for past quarter
    """
    return jsonify(get_relative_rates_for(currency_from, currency_to, 90))


@app.route("/api/prices/yearly/<currency_from>/<currency_to>")
@cache.cached(timeout=64800)
def get_yearly_price_data(currency_from, currency_to):
    """API function for yearly rates data

    Args:
        currency_from: Currency converted from
        currency_to: Currency converted to

    Returns:
        Rates data for past year
    """
    return jsonify(get_yearly_aggregate_data(currency_from, currency_to))
