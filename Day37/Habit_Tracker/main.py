import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# Create a user
# user_params = {
#     "username": USERNAME,
#     "token": TOKEN,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# 
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)
# response.close()

# Create a graph
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# print(response.text)
# response.close()

# Create a pixel

today = str(datetime.today())
date = today.split()[0].replace("-", "")

post_config = {
    "date": date,
    "quantity": "10",
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1", json=post_config, headers=HEADERS)
print(response.text)
response.close()