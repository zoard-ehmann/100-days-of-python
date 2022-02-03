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
        self.all_cities = [
            {
            "city": "Paris",
            "iataCode": "",
            "lowestPrice": 54,
            "id": 2
            },
            {
            "city": "Berlin",
            "iataCode": "",
            "lowestPrice": 42,
            "id": 3
            },
            {
            "city": "Tokyo",
            "iataCode": "TYO",
            "lowestPrice": 485,
            "id": 4
            },
            {
            "city": "Sydney",
            "iataCode": "SYD",
            "lowestPrice": 551,
            "id": 5
            },
            {
            "city": "Istanbul",
            "iataCode": "IST",
            "lowestPrice": 95,
            "id": 6
            },
            {
            "city": "Kuala Lumpur",
            "iataCode": "KUL",
            "lowestPrice": 414,
            "id": 7
            },
            {
            "city": "New York",
            "iataCode": "NYC",
            "lowestPrice": 240,
            "id": 8
            },
            {
            "city": "San Francisco",
            "iataCode": "SFO",
            "lowestPrice": 260,
            "id": 9
            },
            {
            "city": "Cape Town",
            "iataCode": "CPT",
            "lowestPrice": 378,
            "id": 10
            }
        ]
    
    def get_cities(self) -> list:
        """Returns a list of city dictionaries from the spreadsheet with the relevant information

        Returns:
            list: list of city dictionaries with name, lowest price and ID
        """
        # with requests.Session() as session:
        #     response = session.get(url=ST_API, headers=ST_HEADER)
        #     response.raise_for_status()
        #     self.all_cities = response.json()["prices"]
        
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
        
        print(f"{ST_API}/{city_data['id']}")
        print(iata_code)
        #with requests.Session() as session:
        #    response = session.put(url=f"{ST_API}/{city_data['id']}", json=iata_code, headers=ST_HEADER)
        #    response.raise_for_status()