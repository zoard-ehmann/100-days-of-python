import datetime as dt


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_details = {}
    
    def data_collector(self, flight_data: dict):
        if flight_data != None:
            self.flight_details["link"] = flight_data["data"][0]["deep_link"]
            self.flight_details["price"] = flight_data["data"][0]["price"]
            self.flight_details["stations"] = []
            
            for route in flight_data["data"][0]["route"]:
                self.flight_details["stations"].append({
                    "from_city": route["cityFrom"],
                    "from_airport": route["flyFrom"],
                    "from_date": dt.datetime.fromtimestamp(route["dTimeUTC"]).strftime("%Y-%m-%d %H:%M"),
                    "to_city": route["cityTo"],
                    "to_airport": route["flyTo"],
                    "to_date": dt.datetime.fromtimestamp(route["aTimeUTC"]).strftime("%Y-%m-%d %H:%M"),
                })