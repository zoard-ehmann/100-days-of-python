import pandas
import random
import smtplib
import os
from datetime import datetime

from dotenv import load_dotenv


# Load environment variables and define global variables
load_dotenv()
PLACEHOLDER = "[NAME]"
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
smtp_host = os.getenv("SMTP_HOST")
smtp_port = os.getenv("SMTP_PORT")


# Get current month and day
now = datetime.today()

# Read the birthday file and check if someone has birthday today
birthdays = pandas.read_csv("Day32/Automated_Birthday_Wisher/birthdays.csv")
bday_this_month = birthdays[birthdays.month == now.month]
bday_today = bday_this_month[bday_this_month.day == now.day]

# Loop through the list of people who has birthday today
for index, row in bday_today.iterrows():
    # Open the template, insert the name and send the letter
    with open(f"Day32/Automated_Birthday_Wisher/letter_templates/letter_{random.randint(1, 3)}.txt") as template:
        letter = template.read().replace(PLACEHOLDER, row["name"])
        with smtplib.SMTP(smtp_host, smtp_port) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
