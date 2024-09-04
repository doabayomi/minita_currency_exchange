from flask import Flask, render_template, request
import currency
from datetime import date

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        if request.args.get('amount') is None:
            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input=None)
        elif request.args.get('amount') == '':
            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input="invalid")
        else:
            amount = request.args.get('amount')
            currency_from = request.args.get('from')
            currency_to = request.args.get('to')
            converted_amount = currency.convert_currency_at(currency_from,
                                                            currency_to,
                                                            amount,
                                                            date.today())
            answer = {'amount': amount,
                      'currency_from': currency_from,
                      'currency_to': currency_to,
                      'converted_amount': converted_amount}
            
            return render_template("index.html",
                                   currencies=currency.get_currency_list(),
                                   input="valid",
                                   result=answer)
