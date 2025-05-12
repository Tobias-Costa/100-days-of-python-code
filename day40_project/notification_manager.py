import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.addr_email = os.environ["ADDR_EMAIL"]
        self._email_password = os.environ["EMAIL_PASSWORD"]

        # Credentials setup
        # self._account_sid = os.environ["ACCOUNT_SID"]
        # self._auth_token = os.environ["AUTH_TOKEN"]
        # self.from_number = os.environ["FROM_NUMBER"]
        # self.to_number = os.environ["TO_NUMBER"]

    # def send_notification(self, flight_data):
    #     '''This function sends low price alert messages via the Twilio API'''
    #     client = Client(self._account_sid, self._auth_token)
        
    #     message = client.messages.create(
    #     body=f'''
    #     Low price alert! Only £{flight_data.price} to fly 
    #     from {flight_data.origin_airport} to {flight_data.destination_airport},
    #     on {flight_data.out_date} until {flight_data.return_date}.
    #     ''',
    #     from_=self.from_number,
    #     to=self.to_number,
    #     )

    #     print(message.status)

    def send_email(self, email, flight_data):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.addr_email, password=self._email_password)
            connection.sendmail(
                from_addr=self.addr_email,
                to_addrs=email,
                msg=f"Subject: Low price alert!\n\nOnly £{flight_data.price} to fly from {flight_data.origin_airport} to {flight_data.destination_airport}, on {flight_data.out_date} until {flight_data.return_date}.".encode("utf-8")
            )