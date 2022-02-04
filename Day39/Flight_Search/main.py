#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Populate IATA fields if empty
for city in data_manager.get_cities():
    if len(city["iataCode"]) == 0:
        data_manager.insert_iata(city_data=city, city_iata=flight_search.get_iata(city))

# Get cheapest fligths
for city in data_manager.get_cities():
    flight_data = FlightData()
    flight_data.data_collector(flight_search.get_cheapest_flight(city_data=city))
    if flight_data.flight_details["price"] <= city["lowestPrice"]:
        notification_manager.send_msg(flight_data=flight_data)
    print("-----------------------------------------------------------------------------------------------------------")