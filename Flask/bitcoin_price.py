from flask import Flask, render_template_string, request
import requests
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/bitcoin_db")

client = MongoClient(mongo_uri)
db = client.get_database()
bitcoin_collection = db["bitcoin"]

# פונקציה לקבלת המחיר הנוכחי של ביטקוין
def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        usd_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        eur_price = float(data["bpi"]["EUR"]["rate"].replace(",", ""))
        gbp_price = float(data["bpi"]["GBP"]["rate"].replace(",", ""))
        return {"USD": usd_price, "EUR": eur_price, "GBP": gbp_price}
    return None

# פונקציה להמרת דולר לשקלים
def convert_usd_to_ils(usd_price):
    exchange_rate = 3.8  # שער ההמרה לדולר (לדוגמה)
    return usd_price * exchange_rate

# דף הבית
@app.route('/')
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bitcoin Price Tracker</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: url('https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg') no-repeat center center fixed;
                    background-size: cover;
                    color: #000000;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                }
                a {
                    text-decoration: none;
                    color: #000000;
                    font-size: 1.5em;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Bitcoin Price Tracker!</h1>
            <p>Click below to see the current price of Bitcoin:</p>
            <a href="/bitcoin">Check Bitcoin Price</a>
        </body>
        </html>
    """)

# דף מחירי הביטקוין עם אפשרות להמרה
@app.route('/bitcoin', methods=["GET", "POST"])
def bitcoin_price():
    prices = get_bitcoin_price()
    converted_price = None
    target_currency = None

    if request.method == "POST":
        target_currency = request.form.get("currency")
        if target_currency == "ILS":
            converted_price = convert_usd_to_ils(prices["USD"])
        elif target_currency in prices:
            converted_price = prices[target_currency]

    # עיצוב המחירים להוספת פסיקים ושתי ספרות אחרי הנקודה
    if prices:
        for currency in prices:
            prices[currency] = f"{prices[currency]:,.2f}"
        if converted_price:
            converted_price = f"{converted_price:,.2f}"

    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bitcoin Price</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: url('https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg') no-repeat center center fixed;
                    background-size: cover;
                    color: #000000;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                }
                .price {
                    font-size: 2em;
                }
                button {
                    padding: 10px 20px;
                    font-size: 1em;
                    margin: 10px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Bitcoin Price</h1>
            <p class="price">Current Price: ${{ prices['USD'] }} USD</p>
            
            <form method="POST">
                <button type="submit" name="currency" value="EUR">Convert to EUR (€)</button>
                <button type="submit" name="currency" value="GBP">Convert to GBP (£)</button>
                <button type="submit" name="currency" value="ILS">Convert to ILS (₪)</button>
            </form>
            
            {% if converted_price %}
                <p class="price">Converted Price: {{ converted_price }} {{ target_currency }}</p>
            {% endif %}
            
            <a href="/">Go Back</a>
        </body>
        </html>
    """, prices=prices, converted_price=converted_price, target_currency=target_currency)

# הפעלת האפליקציה
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
