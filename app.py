from flask import Flask, render_template, request
import currency

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           currencies=currency.get_currency_list(),
                           current_rates=currency.get_latest_rates())
