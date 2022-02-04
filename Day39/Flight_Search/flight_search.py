import os
import datetime as dt

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
        
    def get_cheapest_flight(self, city_data: dict):
        today = dt.datetime.today()
        trow = (today + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (today + dt.timedelta(days=180)).strftime("%d/%m/%Y")
        tq_params = {
            "fly_from": os.getenv("ORIGIN_CITY"),
            "fly_to": f"city:{city_data['iataCode']}",
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 20,
            "date_from": trow,
            "date_to": six_months,
            "limit": 1,
        }
        
        print(f"Query parameters: {tq_params}")
        with requests.Session() as session:
            response = session.get(url=f"{TQ_API}/search", params=tq_params, headers=TQ_HEADER)
            response.raise_for_status()
            return response.json()