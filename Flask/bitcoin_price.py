from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# פונקציה שמביאה את המחיר הנוכחי של ביטקוין
def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate"]
        return bitcoin_price
    return None

# ראוט לדף הבית
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
                    color: #000000; /* צבע הטקסט שחור */
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                }
                a {
                    text-decoration: none;
                    color: #000000; /* צבע הקישורים שחור */
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

# ראוט לדף שמציג את המחיר של ביטקוין
@app.route('/bitcoin')
def bitcoin_price():
    price = get_bitcoin_price()
    if price:
        return render_template_string(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Bitcoin Price</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background: url('https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg') no-repeat center center fixed;
                        background-size: cover;
                        color: #000000; /* צבע הטקסט שחור */
                        text-align: center;
                        padding: 50px;
                    }}
                    h1 {{
                        font-size: 3em;
                        margin-bottom: 20px;
                    }}
                    .price {{
                        font-size: 2em;
                        color: #000000; /* צבע המחיר שחור */
                    }}
                    a {{
                        text-decoration: none;
                        color: #000000; /* צבע הקישורים שחור */
                        font-size: 1.5em;
                    }}
                    a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <h1>Bitcoin Price</h1>
                <p class="price">${price} USD</p>
                <a href="/">Go Back</a>
            </body>
            </html>
        """)
    else:
        return render_template_string("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background: url('https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg') no-repeat center center fixed;
                        background-size: cover;
                        color: #000000; /* צבע הטקסט שחור */
                        text-align: center;
                        padding: 50px;
                    }
                    h1 {
                        font-size: 3em;
                        color: #ff0000; /* הודעת שגיאה באדום */
                    }
                </style>
            </head>
            <body>
                <h1>Unable to fetch the Bitcoin price.</h1>
                <a href="/">Go Back</a>
            </body>
            </html>
        """)

# הפעלת האפליקציה
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
