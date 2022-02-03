#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch

flight_search = FlightSearch()
flight_search.get_city_codes(["Paris", "London", "Tokyo"])
print(flight_search.city_codes)