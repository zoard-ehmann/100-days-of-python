import smtplib
import requests
import os
import time
from datetime import datetime

from dotenv import load_dotenv


load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
UTC_OFFSET = int(os.getenv("UTC_OFFSET"))
MARGIN = 5


def calculate_local_time(utc_time):
    local_time = utc_time + UTC_OFFSET
    if local_time >= 24:
        return local_time % 24
    elif local_time < 0:
        return 24 + local_time
    return local_time


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = calculate_local_time(int(data["results"]["sunrise"].split("T")[1].split(":")[0]))
    sunset = calculate_local_time(int(data["results"]["sunset"].split("T")[1].split(":")[0]))

    current_hour = datetime.now().hour
    
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    
    return False


def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT - MARGIN <= iss_latitude <= MY_LAT + MARGIN and MY_LONG - MARGIN <= iss_longitude <= MY_LONG + MARGIN:
        return True
    
    return False


while True:
    time.sleep(60)
    if iss_above() and is_dark():
        with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TARGET_EMAIL,
                msg="Subject:Look Up!\n\nThe IIS is on the sky now!"
            )
