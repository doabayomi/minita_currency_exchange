from flask import Flask, render_template, request
import currency
from datetime import date
import os

app = Flask(__name__)
app.config.from_object("config.Config")
news_api_token = app.config['MARKET_AUX_API_KEY']


@app.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        if request.args.get('amount') is None:
            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input="empty")
        elif request.args.get('amount') == '':
            """Invalid input test case"""
            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input="invalid")
        else:
            amount = request.args.get('amount')
            currency_from = request.args.get('from')
            currency_to = request.args.get('to')

            """Exporting chart data"""
            chart_data_path = os.path.join(app.static_folder,
                                           'data',
                                           'chart.json')
            currency.export_data_to_chart(currency_from,
                                          currency_to,
                                          chart_data_path)

            """Exporting conversion data"""
            converted_amount = currency.convert_currency_at(currency_from,
                                                            currency_to,
                                                            amount,
                                                            date.today())
            answer = {'amount': float(amount),
                      'currency_from': currency_from,
                      'currency_to': currency_to,
                      'converted_amount': round(converted_amount, 2)}

            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input="valid",
                                   result=answer)
