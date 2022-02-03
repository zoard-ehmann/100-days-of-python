#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager


data_manager = DataManager()
flight_search = FlightSearch()

all_cities = data_manager.get_cities()
flight_search.populate_iata(cities=all_cities)
