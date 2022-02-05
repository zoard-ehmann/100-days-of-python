import os

import requests
from dotenv import load_dotenv


load_dotenv()

ST_API = os.getenv("ST_API")
ST_HEADER = {
    "Authorization": f"Bearer {os.getenv('ST_TOKEN')}",
    "Content-Type": "application/json",
}


def user_registration(user_mail: str):
    with requests.Session() as session:
        response = session.get(url=ST_API, headers=ST_HEADER)
        response.raise_for_status()
        users = response.json()["users"]
    
    registered_emails = [user["email"] for user in users]
    
    if user_mail in registered_emails:
        print("Your email has been already registered.")
    else:
        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": user_mail,
            }
        }
        
        with requests.Session() as session:
            response = session.post(url=ST_API, json=user_data, headers=ST_HEADER)
            response.raise_for_status()


def validate_mail():
    email = input("What is your email?\n")
    email_ack = input("Type your email again.\n")
    
    if email == email_ack:
        user_registration(user_mail=email)
        print("You're in the club!")
    else:
        print("Email adresses does not match, please try again.")
        validate_mail()


print("Welcome to Zoard's Flight Club!")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

validate_mail()
