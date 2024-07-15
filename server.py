from flask import Flask, jsonify, render_template
from sensor import get_currency_prices

app = Flask(__name__)

@app.route('/prices', methods=['GET'])
def prices():
    prices = get_currency_prices()
    return jsonify(prices)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

