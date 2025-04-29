#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint 
from flight_search import FlightSearch
from data_manager import DataManager

flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_flight_info_sheet()
formatted_data = flight_search.get_iata_code(sheet_data)
pprint(formatted_data)
# data_manager.update_sheet(formated_data)
