import requests
from twilio.rest import Client

FROM_NUMBER = "[CHANGE ME]"
TO_NUMBER = "[CHANGE ME]"

TWILIO_SID = "[CHANGE ME]"
TWILIO_AUTH_TOKEN = "[CHANGE ME]"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "[CHANGE ME]"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY ="[CHANGE ME]"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# GET STOCK PRICES DATA
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

stock_daily_data = [value["4. close"] for (key,value) in data["Time Series (Daily)"].items()]

yesterday_closing_price = stock_daily_data[0]
day_before_yesterday_closing_price = stock_daily_data[1]

stocks_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

if stocks_difference < 0:
    is_increased = False
else:
    is_increased = True

percentage_difference = round(stocks_difference / float(yesterday_closing_price) * 100, 2)

if is_increased:
    stock_notation = f"{STOCK_NAME}: 🔺{percentage_difference}%"
else:
    stock_notation = f"{STOCK_NAME}: 🔻{percentage_difference}%"

print(stock_notation)

if abs(percentage_difference) > 1:
    # GET NEWS
    response = requests.get("https://newsapi.org/v2/everything", params={"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME})
    response.raise_for_status()
    news_data = response.json()["articles"][:3]

    # SEND SMS
    articles_list = [f"{stock_notation}\nHeadline:{article['title']}\nBrief: {article['description']}" for article in news_data]
    for article_message in articles_list:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
        body=article_message,
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        )
        print(message.status)