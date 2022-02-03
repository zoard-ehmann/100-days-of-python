import os

import requests
from dotenv import load_dotenv


load_dotenv()

TQ_API = "https://tequila-api.kiwi.com"
TQ_HEADER = {
    "apikey": os.getenv("TQ_KEY"),
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    
    def get_iata(self, city_data: dict) -> str:
        """Get the IATA code of the city

        Args:
            city (dict): a city dictionary with name, lowest price and ID

        Returns:
            str: city's IATA code
        """
        tq_params = {
            "term": city_data["city"],
            "location_types": "city",
            "limit": 1,
        }
        
        with requests.Session() as session:
            response = session.get(url=f"{TQ_API}/locations/query", params=tq_params, headers=TQ_HEADER)
            response.raise_for_status()
            return response.json()["locations"][0]["code"]