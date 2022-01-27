import smtplib
import os

from dotenv import load_dotenv


load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

with smtplib.SMTP(os.getenv("SMTP"), os.getenv("PORT")) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=os.getenv("TARGET_EMAIL"),
        msg="Subject:Hello\n\nThis is the body of the mail."
    )
