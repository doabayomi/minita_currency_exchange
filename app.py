from flask import Flask, render_template, request, jsonify
from currency_api import (
    get_currency_list,
    get_relative_rates_for,
    export_data_to_chart,
    convert_currency_at
)
import market
from datetime import date
import os
import json

app = Flask(__name__)
app.config.from_object("config.Config")
news_api_token = app.config['MARKET_AUX_API_KEY']


@app.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        if request.args.get('amount') is None:
            return render_template("index.html",
                                   currencies=get_currency_list(),
                                   input="empty")
        elif request.args.get('amount') == '':
            """Invalid input test case"""
            return render_template("index.html",
                                   currencies=get_currency_list(),
                                   input="invalid")
        else:
            amount = request.args.get('amount')
            currency_from = request.args.get('from')
            currency_to = request.args.get('to')

            """Exporting chart data"""
            chart_data_path = os.path.join(app.static_folder,
                                           'data',
                                           'chart.json')
            export_data_to_chart(currency_from, currency_to, chart_data_path)

            """Exporting conversion data"""
            converted_amount = convert_currency_at(currency_from, currency_to,
                                                   amount, date.today())
            answer = {'amount': float(amount),
                      'currency_from': currency_from,
                      'currency_to': currency_to,
                      'converted_amount': round(converted_amount, 2)}

            news_output = market.get_news_for_currencies(currency_from,
                                                         currency_to,
                                                         news_api_token)

            return render_template("index.html",
                                   currencies=get_currency_list(),
                                   input="valid",
                                   result=answer,
                                   news=news_output['data'])


@app.route("/api/prices/weekly/<currency_from>/<currency_to>")
def get_weekly_price_data(currency_from, currency_to):
    return jsonify(get_relative_rates_for(currency_from, currency_to, 7))


@app.route("/api/prices/monthly/<currency_from>/<currency_to>")
def get_monthly_price_data(currency_from, currency_to):
    return jsonify(get_relative_rates_for(currency_from, currency_to, 30))


@app.route("/api/prices/yearly/<currency_from>/<currency_to>")
def get_yearly_price_data(currency_from, currency_to):
    return jsonify(get_relative_rates_for(currency_from, currency_to, 365))
