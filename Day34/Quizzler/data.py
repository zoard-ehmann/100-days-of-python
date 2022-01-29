import requests


API_ENDPOINT = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}


response = requests.get(url=API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()

question_data = response.json()["results"]