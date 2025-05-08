import os
import requests
import datetime
from pprint import pprint 
from dotenv import load_dotenv

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.datetime.now() + datetime.timedelta(days=(6*30))

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

    def get_iata_code(self, city):
        """
        This function takes the name of a city as parameter and returns the IATA code of the corresponding airport through a request to the Amadeus API.
        Returns:
            str: IATA code
        """

        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {"keyword":city, "max":2, "include": "AIRPORTS"}
        response = requests.get(url=IATA_ENDPOINT, params=query, headers=headers)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        code = response.json()["data"][0]['iataCode']

        return code
    
    def search_flights(self, destination):

        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "originLocationCode": "LON",
            "destinationLocationCode": destination,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "returnDate": six_months_from_today.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, params=query, headers=headers)

        if response.status_code != 200:
            print("################ ERROR ################")
            return None
        
        return response.json()




