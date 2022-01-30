import requests
import os

from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

OWM_API_EP = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = os.getenv("OWM_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")

PARAMETERS = {
    "lat": float(os.getenv("LATITUDE")),
    "lon": float(os.getenv("LONGITUDE")),
    "exclude": "current,minutely,daily,alerts",
    "appid": OWM_API_KEY,
}


response = requests.get(url=OWM_API_EP, params=PARAMETERS)
response.raise_for_status()

need_umbrella = False

for hour in response.json()["hourly"][:12]:
    if hour["weather"][0]["id"] < 700:
        need_umbrella = True

if need_umbrella:
    client = Client(TWILIO_SID, TWILIO_API_KEY)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella!",
                        from_=os.getenv("TWILIO_PHONE_NR"),
                        to=os.getenv("PHONE_NR")
                    )

    print(message.status)
