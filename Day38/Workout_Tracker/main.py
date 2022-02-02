import os

import requests
from dotenv import load_dotenv


load_dotenv()

NX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NX_HEADER = {
    "x-app-id": os.getenv("NX_APP_ID"),
    "x-app-key": os.getenv("NX_API_KEY"),
}


nx_params = {
    "query": input("Tell me which excercises you did: ")
}

with requests.Session() as session:
    response = session.post(url=NX_ENDPOINT, json=nx_params, headers=NX_HEADER)
    response.raise_for_status()
    print(response.json())