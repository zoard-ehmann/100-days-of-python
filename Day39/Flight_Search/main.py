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
for city in data_manager.all_cities:
    flight_search = FlightSearch()
    iata = flight_search.get_iata(city)
    print("\n-------------------------------------------------------------------------------------------------------\n")
    
    # Only process cities with valid IATA code
    if len(iata) == 0:
        print(f"City not found: {city['city']} - Ignoring from search...")
    else:
        data_manager.insert_iata(city_data=city, city_iata=iata)
        city["iataCode"] = iata
    
        # Get the cheapest flight to the city
        cheapest_flight = flight_search.get_cheapest_flight(city_data=city, stop_overs=3)

        # Save the most relevant flight details
        if cheapest_flight != None:
            flight = FlightData(flight_data=cheapest_flight)
            
            # Only process the flights within the budget
            if flight.details["price"] <= city["lowestPrice"]:
                print(notification_manager.structure_message(flight_data=flight))
                if EMAIL: notification_manager.send_email(flight_data=flight, users=data_manager.get_subscribers())
                if SMS: notification_manager.send_sms(flight_data=flight)
            else:
                print(f"Only more expensive flights found to {city['city']} than the threshold.")
