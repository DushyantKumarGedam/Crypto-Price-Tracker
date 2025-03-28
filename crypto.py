import requests
import pandas as pd
import matplotlib.pyplot as plt

# API URL for Bitcoin historical market data (30 days)
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"

# Fetch Data
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    # Extract prices (timestamp & price)
    prices = data['prices']

    # Convert to DataFrame
    df = pd.DataFrame(prices, columns=["Timestamp", "Price (USD)"])
    
    # Convert timestamp to readable date
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

    # Display Data
    print(df.head())

    # Plot Price Trend
    plt.figure(figsize=(10, 5))
    plt.plot(df["Timestamp"], df["Price (USD)"], label="Bitcoin Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price Trend (Last 30 Days)")
    plt.legend()
    plt.show()
else:
    print("Error fetching data!")
