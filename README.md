# 📊 Crypto Price Tracker (Live & Historical Data)

## 📌 Project Overview
This Python script fetches **live and historical cryptocurrency price data** using public APIs like **CoinGecko** and **Binance**.  
It can display **Bitcoin’s last 30 days of prices** and plot a graph of its price trends.

## 🔥 Features
✅ Fetch **real-time** and **historical** cryptocurrency prices  
✅ Use **CoinGecko** (simple historical prices) or **Binance** (detailed OHLC data)  
✅ Convert timestamps to **human-readable dates**  
✅ **Plot graphs** of price trends using Matplotlib  
✅ No API key required! (Works with free public APIs)  

## 🛠️ Installation & Setup
### 1️⃣ Install Required Libraries
Before running the script, install the necessary Python packages:

```bash
pip install requests pandas matplotlib
```

### 2️⃣ Run the Python Script
You can choose between **CoinGecko (Simple Price History)** or **Binance (Full OHLC Data)**.

#### **Option 1: Fetch Bitcoin's Last 30 Days of Prices (CoinGecko)**
```bash
python coingecko_price_history.py
```

#### **Option 2: Fetch Bitcoin’s OHLC Data (Binance)**
```bash
python binance_ohlc_history.py
```

## 📜 How It Works
🔹 The script sends a request to the API and retrieves the last 30 days of Bitcoin price data.  
🔹 Converts **timestamps into human-readable dates**.  
🔹 Uses **Pandas** to structure the data and **Matplotlib** to plot the price trend.  

## 📊 Example Output
When you run the script, you’ll see output like this:

```
Timestamp           Price (USD)
---------------------------------
2025-02-27 00:00   42,350.20
2025-02-28 00:00   43,120.55
2025-03-01 00:00   41,780.30
...
```
And a **graph** showing the trend of Bitcoin’s price over the last 30 days!

## 🌎 API Sources
- **[CoinGecko API](https://www.coingecko.com/en/api/documentation)** – For simple historical price data  
- **[Binance API](https://binance-docs.github.io/apidocs/spot/en/)** – For detailed OHLC (candlestick) data  

## 🚀 Future Enhancements
🔹 Add support for **multiple cryptocurrencies** (Ethereum, Dogecoin, Solana, etc.)  
🔹 Fetch **real-time prices** every minute/hour  
🔹 Store data in a **CSV file or database**  
🔹 Create a **web dashboard** for live price tracking  

## 📝 License
This project is **open-source** and free to use! Feel free to modify and improve it. 🚀  
