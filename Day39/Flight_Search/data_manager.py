import os

import requests
from dotenv import load_dotenv


load_dotenv()

ST_API = os.getenv("ST_API")
ST_HEADER = {
    "Authorization": f"Bearer {os.getenv('ST_TOKEN')}",
    "Content-Type": "application/json",
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.all_cities: list
    
    def get_cities(self) -> list:
        """Returns a list of city dictionaries from the spreadsheet with the relevant information

        Returns:
            list: list of city dictionaries with name, lowest price and ID
        """
        with requests.Session() as session:
            response = session.get(url=ST_API, headers=ST_HEADER)
            response.raise_for_status()
            self.all_cities = response.json()["prices"]
        
        return self.all_cities
    
    def insert_iata(self, city_data: list):
        """Inserts IATA code for every city on the list

        Args:
            city_data (list): list of city dictionaries with ID and IATA
        """
        for city in self.all_cities:
            
            city_iata = {
                "price": {
                    "iataCode": city_data[city["id"]]
                }
            }
            
            with requests.Session() as session:
                response = session.put(url=f"{ST_API}/{city['id']}", json=city_iata, headers=ST_HEADER)
                response.raise_for_status()