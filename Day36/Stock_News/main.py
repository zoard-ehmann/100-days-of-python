import os
import re
import requests

from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

TAG_RE = re.compile(r'<[^>]+>')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API = f"https://www.alphavantage.co/query"
AV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": os.getenv("AV_KEY"),
}


def remove_tags(text):
    return TAG_RE.sub("", text)


def send_alert(title: str, brief: str, article: str):
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_KEY")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"{STOCK}: {direction}{diff}%\n\nTitle: {title}\n\nBrief: {brief}\n\nArticle: {article}",
                        from_=os.getenv("TWILIO_PHONE_NR"),
                        to=os.getenv("PHONE_NR")
                    )

    print(message.status)


def get_news():
    newsapi = NewsApiClient(api_key=os.getenv("NEWS_KEY"))

    all_articles = newsapi.get_everything(q=COMPANY_NAME, language='en')
    recent_news = all_articles["articles"][:3]

    for news in recent_news:
        send_alert(news["title"], remove_tags(news["description"], news["url"]))


with requests.Session() as s:
    download = s.get(url=AV_API, params=AV_PARAMS)
    download.raise_for_status()
    stock_data = download.json()

last_two_days = list(stock_data["Time Series (Daily)"].items())[:2]
day_zero = float(last_two_days[0][1]["4. close"])
day_minus_one = float(last_two_days[-1][1]["4. close"])
diff = round(abs(100 - (day_zero / day_minus_one * 100)))

if diff >= 5:
    if day_zero > day_minus_one:
        direction = "🔺"
    else:
        direction = "🔻"
    get_news()
