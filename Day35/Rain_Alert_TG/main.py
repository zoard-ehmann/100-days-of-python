import requests
import os

from dotenv import load_dotenv


load_dotenv()

OWM_API_EP = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = os.getenv("OWM_API_KEY")
OWM_PARAMETERS = {
    "lat": float(os.getenv("LATITUDE")),
    "lon": float(os.getenv("LONGITUDE")),
    "exclude": "current,minutely,daily,alerts",
    "appid": OWM_API_KEY,
}
TG_TOKEN = os.getenv("TG_TOKEN")
TG_API_EP = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
TG_DATA = {
    "chat_id": os.getenv("TG_CHAT_ID"),
    "text": "It's going to rain today. Do not forget to bring an umbrella!",
}


response = requests.get(url=OWM_API_EP, params=OWM_PARAMETERS)
response.raise_for_status()

need_umbrella = False

for hour in response.json()["hourly"][:12]:
    if hour["weather"][0]["id"] < 700:
        need_umbrella = True

if need_umbrella:
    request = requests.post(url=TG_API_EP, data=TG_DATA)
    request.raise_for_status()
