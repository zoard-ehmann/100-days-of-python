#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


EMAIL = True
SMS = False


data_manager = DataManager()
notification_manager = NotificationManager()

# Populate IATA fields if empty
for city in data_manager.get_cities():
    if len(city["iataCode"]) == 0:
        flight_search = FlightSearch()
        data_manager.insert_iata(city_data=city, city_iata=flight_search.get_iata(city))

# Get cheapest fligths
for city in data_manager.get_cities():
    if len(city["iataCode"]) != 0:
        flight_search = FlightSearch()
        flight_data = FlightData()
        
        cheapest_flight = flight_search.get_cheapest_flight(city_data=city, stop_overs=3)
        flight_data.data_collector(cheapest_flight)
        
        if len(flight_data.flight_details) != 0 and flight_data.flight_details["price"] <= city["lowestPrice"]:
            print(notification_manager.structure_message(flight_data=flight_data))
            if EMAIL: notification_manager.send_email(flight_data=flight_data, users=data_manager.get_subscribers())
            if SMS: notification_manager.send_sms(flight_data=flight_data)
