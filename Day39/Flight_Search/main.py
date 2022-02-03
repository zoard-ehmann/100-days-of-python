#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager


data_manager = DataManager()
flight_search = FlightSearch()

all_cities = data_manager.get_cities()

for city in all_cities:
    if len(city["iataCode"]) == 0:
        data_manager.insert_iata(city_data=city, city_iata=flight_search.get_iata(city))
