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
        self.city_codes = []
    
    def get_city_codes(self, cities: list):
        """Collects the city codes of the passed in cities into a list

        Args:
            cities (list): a list of city names
        """
        
        tq_params = {
            "location_types": "city",
            "limit": 1,
        }
        
        for city in cities:
            tq_params["term"] = city
            with requests.Session() as session:
                response = session.get(url=f"{TQ_API}/locations/query", params=tq_params, headers=TQ_HEADER)
                response.raise_for_status()
                self.city_codes.append(response.json()["locations"][0]["code"])