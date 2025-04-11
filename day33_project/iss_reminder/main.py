import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "[CHANGE ME]"
MY_PASSWORD = "[CHANGE ME]"

MY_LONGITUDE = "[CHANGE ME]"
MY_LATITUDE =  "[CHANGE ME]"

def is_iss_over_my_head():
    '''Check if the ISS is close to me'''

    #Get ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    
    if MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5 and MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5:
        return True

def is_night():
    '''Check if it's dark'''

    #Get sunrise and sunset hour
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour
    
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    
while True:
    if is_iss_over_my_head() and is_night():
        #Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Look up\n\nThe ISS is above you now!".encode("utf-8")
                )
    time.sleep(60)