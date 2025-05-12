#Imports
import time
from pprint import pprint 
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight

# Conditional variable initialized
was_changed = False

# Objects setup
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

#Get datasheet's info
data_sheet = data_manager.get_flight_info_sheet()
pprint(data_sheet)

#Check if the IATA code is not empty in the data sheet
for data in data_sheet:

    # If the code field is empty, it will change to the correct one.
    if data["iataCode"] == "":

        was_changed = True
        city = data["city"]

        try:
            iata_code = flight_search.get_iata_code(city)
            data["iataCode"] = iata_code
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            data["iataCode"] = "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            data["iataCode"] = "N/A"

        time.sleep(2)

# Debugation print
pprint(data_sheet)

# Check if the datasheet has been updated locally. If yes, it will update the datasheet in google sheet
if was_changed:
    data_manager.update_sheet(data_sheet)

customers_data = data_manager.get_customer_emails()
customers_email = [customer["what'sYourEmail?"] for customer in customers_data]

for destination in data_sheet:
    #Get flight prices
    print(f"Getting flights for {destination['city']}...")

    flights = flight_search.search_flights(destination["iataCode"])
    cheapest_flight = find_cheapest_flight(flights)

    # If there are no direct flights, the program will look for flights with stopovers.
    if cheapest_flight.price == "N/A":
        print("No direct flights. Searching for flights with stopovers...")
        flights = flight_search.search_flights(destination["iataCode"], is_direct=False)
        cheapest_flight = find_cheapest_flight(flights)

    print(f"{destination['city']}: £{cheapest_flight.price}")

    # Sending SMS in case of low price
    # if cheapest_flight.price != "N/A" and cheapest_flight.price < float(destination["lowestPrice"]):
    #     print(f"Lower price flight found to {destination['city']}!")
    #     notification_manager.send_notification(cheapest_flight)

    # Sending email in case of low price
    if cheapest_flight.price != "N/A" and cheapest_flight.price < float(destination["lowestPrice"]):

        print(f"Lower price flight found to {destination['city']}!")

        for email in customers_email:
            notification_manager.send_email(email, cheapest_flight)

    # Slowing down requests to avoid rate limit
    time.sleep(2)
