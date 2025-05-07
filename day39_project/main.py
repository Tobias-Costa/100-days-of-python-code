#Imports
import time
from pprint import pprint 
from flight_search import FlightSearch
from data_manager import DataManager

# Conditional variable initialized
was_changed = False

# Objects setup
flight_search = FlightSearch()
data_manager = DataManager()

#Get datasheet's info
data_sheet = data_manager.get_flight_info_sheet()

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
    # was_changed = False