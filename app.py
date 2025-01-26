from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

def get_supported_currencies():
    response = requests.get(f"{COINGECKO_API_URL}/simple/supported_vs_currencies")
    return response.json()

def get_crypto_list():
    response = requests.get(f"{COINGECKO_API_URL}/coins/list")
    return response.json()

def get_conversion_rate(crypto_id, target_currency):
    response = requests.get(
        f"{COINGECKO_API_URL}/simple/price",
        params={
            "ids": crypto_id,
            "vs_currencies": target_currency
        }
    )
    return response.json()

@app.route('/')
def index():
    crypto_list = get_crypto_list()
    currencies = get_supported_currencies()
    return render_template('index.html', 
                         cryptocurrencies=crypto_list,
                         currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    crypto_id = data.get('crypto_id')
    target_currency = data.get('target_currency')
    amount = float(data.get('amount', 1.0))

    try:
        conversion_data = get_conversion_rate(crypto_id, target_currency)
        if crypto_id in conversion_data:
            rate = conversion_data[crypto_id][target_currency]
            converted_amount = rate * amount
            return jsonify({
                'success': True,
                'result': converted_amount,
                'rate': rate,
                'timestamp': datetime.now().isoformat()
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
