import requests
import os
from requests.auth import HTTPBasicAuth
from pprint import pprint 
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._prices_sheety_endpoint = os.environ["PRICES_SHEETY_ENDPOINT"]
        self._users_sheety_endpoint = os.environ["USERS_SHEETY_ENDPOINT"]
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)

    def get_flight_info_sheet(self):
        # Get and return the data stored in the google sheet
        response = requests.get(url=self._prices_sheety_endpoint, auth=self._authorization)
        response.raise_for_status()

        data_sheet = response.json()["prices"]

        return data_sheet
    
    def update_sheet(self, data_sheet):
        for row in data_sheet:

            update_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            object_id = row["id"]
            final_put_endpoint = f"{self._prices_sheety_endpoint}/{object_id}"
            
            response = requests.put(url=final_put_endpoint, json=update_data, auth=self._authorization)
            response.raise_for_status()
            pprint(response.json())

    def get_customer_emails(self):

        response = requests.get(url=self._users_sheety_endpoint, auth=self._authorization)
        response.raise_for_status()

        customers_sheet = response.json()["users"]

        return customers_sheet