import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData

load_dotenv()

TW_SID = os.getenv("TW_SID")
TW_KEY = os.getenv("TW_KEY")
TW_PHONE_NR = os.getenv("TW_PHONE_NR")
PHONE_NR = os.getenv("PHONE_NR")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TW_SID, TW_KEY)
        
    def send_msg(self, flight_data: FlightData):
        msg_segments = [f"Price: {flight_data.flight_details['price']} EUR"]
        for station in flight_data.flight_details["stations"]:
            msg_segments.append(f"From {station['from_city']}({station['from_airport']}) to {station['to_city']}({station['to_airport']})")
            msg_segments.append(f"{station['from_date']} - {station['to_date']} (UTC)")
        final_msg = "\n".join(msg_segments)
        print(f"Message body: {final_msg}")
        
        
        message = self.client.messages.create(
            body=f"Cheap flight!\n\n{final_msg}",
            from_=TW_PHONE_NR,
            to=PHONE_NR,
        )
        
        print(f"Message status: {message.status}")