import os
import requests
import time
from dotenv import load_dotenv

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        """
        Initialize an instance of the FlightSearch class.
        This constructor performs the following tasks:
        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.
        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token method.
        """
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]

    def get_iata_code(self, sheet_data):
        for data in sheet_data:

            print(f"Using this token to get destination {self._token}")
            headers = {"Authorization": f"Bearer {self._token}"}

            if data["iataCode"] == "":

                city_name = data["city"]
                query = {"keyword":city_name, "max":2, "include": "AIRPORTS"}
                response = requests.get(url=IATA_ENDPOINT, params=query, headers=headers)
                print(f"Status code {response.status_code}. Airport IATA: {response.text}")

                try:
                    iata_code = response.json()["data"][0]['iataCode']
                    data["iataCode"] = iata_code
                except IndexError:
                    print(f"IndexError: No airport code found for {city_name}.")
                    data["iataCode"] = "N/A"
                except KeyError:
                    print(f"KeyError: No airport code found for {city_name}.")
                    data["iataCode"] = "N/A"

                time.sleep(2)
            
        return sheet_data