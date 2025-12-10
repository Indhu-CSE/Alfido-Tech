import requests

# -----------------------------------
# WEATHER API
# -----------------------------------
def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=649bf02e7d9f2d9c0d818f8468555e28&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print("Error:", data.get("message"))
            return

        print("\n----- WEATHER REPORT -----")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"])
        print("Weather:", data["weather"][0]["description"])

    except Exception as e:
        print("Something went wrong:", e)


# -----------------------------------
# CRYPTO PRICE API
# -----------------------------------
def get_crypto_price(crypto_name):
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 250,
            "page": 1,
        }
        response = requests.get(url, params=params)
        data = response.json()

        crypto_name = crypto_name.lower()
        for coin in data:
            if crypto_name in coin["name"].lower():
                print("\n----- CRYPTO PRICE -----")
                print("Name:", coin["name"])
                print("Symbol:", coin["symbol"])
                print("Current Price:", coin["current_price"], "USD")
                print("Market Cap:", coin["market_cap"])
                return

        print("Crypto not found!")

    except Exception as e:
        print("Something went wrong:", e)


# -----------------------------------
# NEWS API
# -----------------------------------
def get_news(keyword):
    try:
        url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=62768d89c27e4cf794e94bbd227ff2f5"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            print("Error fetching news")
            return

        print("\n----- NEWS RESULTS -----")
        for i, article in enumerate(data["articles"][:5]):
            print(f"\n{i+1}. {article['title']}")
            print("Source:", article['source']['name'])
            print("URL:", article['url'])

    except Exception as e:
        print("Something went wrong:", e)


# -----------------------------------
# MAIN MENU
# -----------------------------------
def main():
    while True:
        print("\n====== API Integration Tool ======")
        print("1. Weather Search")
        print("2. Crypto Price Search")
        print("3. News Search")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            get_weather(city)

        elif choice == "2":
            crypto = input("Enter crypto name: ")
            get_crypto_price(crypto)

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            get_news(keyword)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
