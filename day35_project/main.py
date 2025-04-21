import requests
from twilio.rest import Client
API_KEY = "[CHANGE ME]"
LATITUDE = "[CHANGE ME]"
LONGITUDE = "[CHANGE ME]"
FROM_NUMBER = "[CHANGE ME]"
TO_NUMBER = "[CHANGE ME]"

account_sid = "[CHANGE ME]"
auth_token = "[CHANGE ME]"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

condition_codes = [weather_data["list"][i]["weather"][0]["id"] for i in range(4)]

for code in condition_codes:
    if int(code) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        )
        print(message.status)
        break