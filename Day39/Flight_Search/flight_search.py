import os
import pprint
import datetime as dt

import requests
from dotenv import load_dotenv


load_dotenv()
pp = pprint.PrettyPrinter(indent=4)

TQ_API = "https://tequila-api.kiwi.com"
TQ_HEADER = {
    "apikey": os.getenv("TQ_KEY"),
}
MIN_NIGHTS = 7
MAX_NIGHTS = 28
MAX_STOPOVERS = 0
STOPOVER_CITIES = ""


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight = None
    
    def get_iata(self, city_data: dict) -> str:
        """Gets the IATA code of the city.

        Args:
            city (dict): A city dictionary with name, lowest price and ID.

        Returns:
            str: City's IATA code.
        """
        tq_params = {
            "term": city_data["city"],
            "location_types": "city",
            "limit": 1,
        }
        
        with requests.Session() as session:
            response = session.get(url=f"{TQ_API}/locations/query", params=tq_params, headers=TQ_HEADER)
            response.raise_for_status()
            
            try:
                city_iata = response.json()["locations"][0]["code"]
            except IndexError:
                city_iata = ""
            
            return city_iata
        
    def get_cheapest_flight(self, city_data: dict, stop_overs: int = MAX_STOPOVERS, via_city: str = STOPOVER_CITIES) -> dict:
        """Gets the cheapest flight to a particular city.

        Args:
            city_data (dict): Details of the target city.
            stop_overs (int, optional): Number of maximum stop-overs. Defaults to MAX_STOPOVERS.
            via_city (str, optional): Stop-over airports as comma-separated values. Defaults to STOPOVER_CITIES.

        Returns:
            dict: Details of the flight as a dictionary.
        """
        today = dt.datetime.today()
        trow = (today + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (today + dt.timedelta(days=180)).strftime("%d/%m/%Y")
        tq_params = {
            "fly_from": os.getenv("ORIGIN_CITY"),
            "fly_to": f"city:{city_data['iataCode']}",
            "nights_in_dst_from": MIN_NIGHTS,
            "nights_in_dst_to": MAX_NIGHTS,
            "date_from": trow,
            "date_to": six_months,
            "limit": 1,
            "max_stopovers": stop_overs,
            "select_stop_airport": via_city,
        }
        
        with requests.Session() as session:
            response = session.get(url=f"{TQ_API}/search", params=tq_params, headers=TQ_HEADER)
            response.raise_for_status()
            flight = response.json()
            
            if flight["_results"] != 0:
                self.flight = flight
        
        return self.flight