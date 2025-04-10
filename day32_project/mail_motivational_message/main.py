import smtplib
from random import choice
import datetime as dt

MY_EMAIL = "[CHANGE ME]"
PASSWORD = "[CHANGE ME]"

now = dt.datetime.now()
week_day = now.weekday()

def send_mail(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Motivational Message\n\n{quote}".encode("utf-8")
        )

with open("./quotes.txt", encoding="utf-8") as data:
    quotes_lst = [line.strip("\n") for line in data.readlines()]
    random_quote = choice(quotes_lst)

if week_day == 0: # Starts counting from Monday (Monday = 0)
    send_mail(random_quote)