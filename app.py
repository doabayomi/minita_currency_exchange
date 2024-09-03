from flask import Flask, render_template, url_for
import currency

app = Flask(__name__)


@app.route("/")
def index():
    currency_list = currency.get_list()
    latest_prices = currency.get_latest_prices()
    return render_template("index.html", currency_list=currency_list,
                           latest_prices=latest_prices)
