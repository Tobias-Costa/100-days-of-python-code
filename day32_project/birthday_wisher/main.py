import smtplib
import pandas as pd
import datetime as dt
from random import randint

MY_EMAIL = "[CHANGE ME]"
PASSWORD = "[CHANGE ME]"

def send_mail(addrs_name, addrs_email, letter):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=addrs_email,
            msg=f"Subject: Happy Birthday {addrs_name}!\n\n{letter}".encode("utf-8")
        )

data_file = pd.read_csv("birthdays.csv")
birthdays_dict = data_file.to_dict(orient="records")
now = dt.datetime.now()

for b in birthdays_dict:
    if now.month == b["month"] and now.day == b["day"]:
        #Addressee's name and email
        addressee_email = b["email"]
        addressee_name = b["name"]
        #Use .randint() to choose the card and use .replace() on the card
        choosen_letter = f"letter_{randint(1,3)}.txt"
        with open(f"./letter_templates/{choosen_letter}", encoding="utf-8") as content:
            letter = content.read()
            new_letter = letter.replace("[NAME]", addressee_name)
        # Send mail
        send_mail(addressee_name, addressee_email, new_letter)