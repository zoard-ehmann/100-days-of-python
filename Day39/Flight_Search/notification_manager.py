import os
import smtplib

from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData

load_dotenv()

TW_SID = os.getenv("TW_SID")
TW_KEY = os.getenv("TW_KEY")
TW_PHONE_NR = os.getenv("TW_PHONE_NR")
PHONE_NR = os.getenv("PHONE_NR")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_client = Client(TW_SID, TW_KEY)
        
    def structure_message(self, flight_data: FlightData) -> str:
        """Gets the most relevant data of the flight and format the notification message.

        Args:
            flight_data (FlightData): The most relevant data of the flight as a FlightData object.

        Returns:
            str: Formatted notification message.
        """
        currency = "EUR" #TODO: use EUR symbol
        msg_segments = [f"Price: {flight_data.details['price']}{currency}\n"]
        
        for station in flight_data.details["stations"]:
            msg_segments.append(f"From {station['from_city']}({station['from_airport']}) to {station['to_city']}({station['to_airport']})")
            msg_segments.append(f"{station['from_date']} - {station['to_date']} (UTC)\n")
            
        msg_segments.append(flight_data.details["link"])
        final_msg = "\n".join(msg_segments)
        return final_msg

    def send_sms(self, flight_data: FlightData):
        """Gets the most relevant data of the flight for further formatting and sends an SMS alert.

        Args:
            flight_data (FlightData): The most relevant data of the flight as a FlightData object.
        """
        final_message = self.structure_message(flight_data=flight_data)
        
        message = self.twilio_client.messages.create(
            body=f"Cheap flight!\n\n{final_message}",
            from_=TW_PHONE_NR,
            to=PHONE_NR,
        )

    def send_email(self, flight_data: FlightData, users: list):
        """Gets the most relevant data of the flight for further formatting and sends an Email alert for all the subscribed users.

        Args:
            flight_data (FlightData): The most relevant data of the flight as a FlightData object.
            users (list): List of the user dictionaries with first name, last name and email address.
        """
        final_message = self.structure_message(flight_data=flight_data)
        
        for user in users:
            with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user["email"],
                    msg=f"Subject:Cheap Flight Alert!\n\n{final_message}"
                )