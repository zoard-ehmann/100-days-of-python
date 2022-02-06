import datetime as dt


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_data: dict):
        """Collects the most relevant data of the flight and stores it as a dictionary.

        Args:
            flight_data (dict): Returned flight details from Tequila API.
        """
        self.details = {
            "link": flight_data["data"][0]["deep_link"],
            "price": flight_data["data"][0]["price"],
            "stations": [],
        }
        self.__populate_stations(flight_route=flight_data["data"][0]["route"])
    
    def __populate_stations(self, flight_route: list):
        """Populates the stations field of the flight details dictionary.

        Args:
            flight_route (list): Flight route as a list.
        """
        for route in flight_route:
            self.details["stations"].append({
                "from_city": route["cityFrom"],
                "from_airport": route["flyFrom"],
                "from_date": dt.datetime.fromtimestamp(route["dTimeUTC"]).strftime("%Y-%m-%d %H:%M"),
                "to_city": route["cityTo"],
                "to_airport": route["flyTo"],
                "to_date": dt.datetime.fromtimestamp(route["aTimeUTC"]).strftime("%Y-%m-%d %H:%M"),
            })
