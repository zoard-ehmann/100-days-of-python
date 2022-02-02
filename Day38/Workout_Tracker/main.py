import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()

NX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NX_HEADER = {
    "x-app-id": os.getenv("NX_APP_ID"),
    "x-app-key": os.getenv("NX_API_KEY"),
}

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_HEADER = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}",
    "Content-Type": "application/json"
}


now = datetime.now()
nx_params = {
    "query": input("Tell me which excercises you did: "),
    "gender": os.getenv("GENDER"),
    "weight_kg": os.getenv("WEIGHT_KG"),
    "height_cm": os.getenv("HEIGHT_CM"),
    "age": os.getenv("AGE"),
}

with requests.Session() as session:
    response = session.post(url=NX_ENDPOINT, json=nx_params, headers=NX_HEADER)
    response.raise_for_status()
    exercise_info = response.json()

for exercise in exercise_info["exercises"]:
    new_workout = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].capitalize(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    
    with requests.Session() as session:
        response = session.post(url=SHEETY_ENDPOINT, json=new_workout, headers=SHEETY_HEADER)
        response.raise_for_status()
