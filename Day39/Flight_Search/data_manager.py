import os
from urllib import response

import requests
from dotenv import load_dotenv


load_dotenv()

ST_API_PRICES = os.getenv("ST_API_PRICES")
ST_API_USERS = os.getenv("ST_API_USERS")
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
            response = session.get(url=ST_API_PRICES, headers=ST_HEADER)
            response.raise_for_status()
            self.all_cities = response.json()["prices"]
        
        return self.all_cities
    
    def insert_iata(self, city_data: dict, city_iata: str):
        """Inserts IATA code for the corresponding city

        Args:
            city_data (dict): a city dictionary with name, lowest price and ID
            city_iata (str): IATA code for the city
        """
        iata_code = {
            "price": {
                "iataCode": city_iata
            }
        }
        
        with requests.Session() as session:
            response = session.put(url=f"{ST_API_PRICES}/{city_data['id']}", json=iata_code, headers=ST_HEADER)
            response.raise_for_status()
        
    def get_subscribers(self):
        with requests.Session() as session:
            response = session.get(url=f"{ST_API_USERS}", headers=ST_HEADER)
            response.raise_for_status()
            return response.json()["users"]
            