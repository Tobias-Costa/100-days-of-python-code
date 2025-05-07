import requests
import os
from requests.auth import HTTPBasicAuth
from pprint import pprint 
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/c9c0690c87d1263a1eeffb1d213b6465/flightDeal/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)

    def get_flight_info_sheet(self):
        # Get and return the data stored in the google sheet
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        response.raise_for_status()

        data_sheet = response.json()["prices"]
        pprint(data_sheet)

        return data_sheet
    
    def update_sheet(self, data_sheet):
        for row in data_sheet:

            update_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            object_id = row["id"]
            final_put_endpoint = f"{SHEETY_ENDPOINT}/{object_id}"
            
            response = requests.put(url=final_put_endpoint, json=update_data, auth=self._authorization)
            response.raise_for_status()
            pprint(response.json())