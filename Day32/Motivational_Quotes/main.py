import os
import random
import smtplib
import datetime as dt

from dotenv import load_dotenv


load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("PASSWORD")
smtp_host = os.getenv("SMTP")
smtp_port = os.getenv("PORT")
target_email = os.getenv("TARGET_EMAIL")

if dt.datetime.today().weekday() == 3:
    with open("Day32/Motivational_Quotes/quotes.txt") as file:
        quotes = file.readlines()

    weekly_quote = random.choice(quotes)

    with smtplib.SMTP(host=smtp_host, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:Weekly Motivation\n\n{weekly_quote}"
        )