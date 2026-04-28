# 📈 StockAI — AI Stock Prediction Dashboard

A full-stack stock analytics and prediction platform that combines real-time financial data with machine learning to forecast stock price trends. Built with a modern React frontend and a Flask-based backend API.

---

## 🚀 Features

* 📊 **Real-time Stock Data** using Yahoo Finance (`yfinance`)
* 🤖 **ML-Based Prediction** using Linear Regression
* 📈 **Next-Day Price Forecasting** with confidence score
* 🔍 **Dynamic Stock Search** (AAPL, TSLA, etc.)
* ⚡ **REST API Integration** between frontend and backend
* 🎯 **Interactive Dashboard UI**

---

## 🛠 Tech Stack

**Frontend**

* React.js
* JavaScript (ES6+)
* Fetch API

**Backend**

* Flask
* Flask-CORS

**Machine Learning**

* Scikit-learn (Linear Regression)
* NumPy

**Data Source**

* yfinance (Yahoo Finance API)

---

## 🧠 How It Works

1. User enters a stock symbol (e.g., TSLA)
2. Backend fetches historical data using `yfinance`
3. Linear Regression model is trained on closing prices
4. Model predicts the **next day's price**
5. Response is sent to frontend and displayed on dashboard

---

## 📊 API Example

**Endpoint:**

```
GET /predict?symbol=AAPL
```

**Response:**

```json
{
  "prediction": 185.23,
  "confidence": 0.92
}
```

---

## ▶️ Run Locally

### 🔹 Backend (Flask)

```bash
cd backend
python app.py
```

Runs on:

```
http://127.0.0.1:5000
```

---

### 🔹 Frontend (React)

```bash
cd frontend
npm install
npm start
```

Runs on:

```
http://localhost:3000
```

---

## 📁 Project Structure

```
StockAi/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── (React app files)
│
├── README.md
└── .gitignore
```

---

## ⚠️ Disclaimer

This project is for educational purposes only. The predictions are based on simple machine learning models and should not be used for real financial decision-making.

---

## 🔥 Future Improvements

* 📉 Advanced ML models (LSTM / Time Series Forecasting)
* 📊 Interactive charts (Recharts / Chart.js)
* 🌐 Deployment (Vercel + Render)
* 📱 Responsive UI improvements

---

## 👨‍💻 Author

**Ayushman Kumar**
Final-Year Data Science Student

---

## ⭐ If you like this project

Give it a star on GitHub ⭐ — it helps a lot!
