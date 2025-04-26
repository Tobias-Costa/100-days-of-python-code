import requests
from datetime import datetime

APP_ID = "[CHANGE_ME]"
API_KEY = "[CHANGE_ME]"

GENDER = "[CHANGE_ME]"
WEIGHT_KG = "[CHANGE_ME]"
HEIGHT_CM = "[CHANGE_ME]"
AGE = "[CHANGE_ME]"

NUTRITIONIX_ENDPOINT = 	"https://trackapi.nutritionix.com/v2/natural/exercise" #https://www.nutritionix.com/business/api
SHEETY_ENDPOINT = "[CHANGE_ME]" #https://sheety.co/

bearer_headers = {"Authorization": "Bearer [CHANGE_ME]"}

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Describe what exercises do you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE ,         
              }

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters,headers=nutritionix_headers)
response.raise_for_status()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

for exercise in response.json()["exercises"]:
    sheety_parameters = {
        "workout" : {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=bearer_headers)
    sheety_response.raise_for_status()