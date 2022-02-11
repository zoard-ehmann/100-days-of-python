import pprint
import smtplib
import os

import lxml
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()

AZ_URL = 'https://www.amazon.com/Wacom-Cintiq-Pro-Creative-Display/dp/B07BDDYK99/ref=sr_1_3?keywords=wacom+cintiq+pro+24&qid=1644561359&sprefix=wacom+cint%2Caps%2C174&sr=8-3'
AZ_HEADER = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
}
MAX_PRICE = 1800

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
SMTP = os.getenv('SMTP')
PORT = os.getenv('PORT')


pp = pprint.PrettyPrinter()

with requests.Session() as session:
    response = session.get(url=AZ_URL, headers=AZ_HEADER)
    response.raise_for_status()
    site_data = response.text

soup = BeautifulSoup(site_data, 'lxml')

product_name = soup.find(name='span', id='productTitle').getText().strip()
price = float(soup.find(name='span', class_='a-offscreen').getText().strip('$').replace(',', ''))

if price < MAX_PRICE:
    with smtplib.SMTP(host=SMTP, port=PORT) as smtp:
        smtp.starttls()
        smtp.login(
            user=EMAIL,
            password=PASSWORD,
        )
        smtp.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject:Amazon Price Alert!\n\n{product_name} is now ${price}.\n{AZ_URL}'.encode('utf-8')
        )
