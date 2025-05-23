import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

URL = os.environ["PRODUCT_URL"]
ALERT_PRICE = 100

addr_email = os.environ["ADDR_EMAIL"]
email_password = os.environ["EMAIL_PASSWORD"]

def send_mail(product_title, current_price, product_link):
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=addr_email
        , password=email_password)
            connection.sendmail(
                from_addr=addr_email
            ,
                to_addrs=addr_email
            ,
                msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now ${current_price}\n\n{product_link}".encode("utf-8")
                )

header = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

price = float(soup.find(class_="a-offscreen").getText().replace(",",".").strip("R$ "))
print(price)

if price <= ALERT_PRICE:

    product_title = " ".join(soup.find(id="productTitle").get_text().strip())

    send_mail(product_title, price, URL)