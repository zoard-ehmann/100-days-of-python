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
    
    def populate_iata(self, cities: list) -> list:
        """Populates city IATA codes of the passed in city dictionary entries and returns the new list

        Args:
            cities (list): a list of city dictionaries with name, lowest price and ID

        Returns:
            list: a list of city dictionaries with ID and IATA
        """
        
        complete_cities = {}
        tq_params = {
            "location_types": "city",
            "limit": 1,
        }
        
        for city_data in cities:
            tq_params["term"] = city_data["city"]
            
            with requests.Session() as session:
                response = session.get(url=f"{TQ_API}/locations/query", params=tq_params, headers=TQ_HEADER)
                response.raise_for_status()
                city_code = response.json()["locations"][0]["code"]
                city_data["iataCode"] = city_code
                
            complete_cities[city_data["id"]] = city_code
        
        return complete_cities
            