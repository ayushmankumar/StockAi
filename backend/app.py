from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Stock ML API running 🚀"

@app.route("/predict", methods=["GET"])
def predict():
    symbol = request.args.get("symbol")

    stock = yf.download(symbol, period="1mo")

    if stock.empty:
        return jsonify({"error": "Invalid stock"}), 400

    prices = stock["Close"].values

    X = np.arange(len(prices)).reshape(-1, 1)
    y = prices

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)[0]

    confidence = model.score(X, y)

    return jsonify({
        "prediction": round(float(prediction), 2),
        "confidence": round(float(confidence), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)