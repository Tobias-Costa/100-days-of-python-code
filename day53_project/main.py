import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Make a soup of the zillow.com
headers = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers)
response.raise_for_status()

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

all_homes = soup.select("div .StyledPropertyCardDataWrapper")

#Scrape and create a list of address
home_address = [home.find("address").get_text().replace(" | ", " ").strip() for home in all_homes]

#Scrape and create a list of property's prices(e.g.: $443)
home_prices = [home.find("span", class_="PropertyCardWrapper__StyledPriceLine").get_text().replace("/mo", "").split("+")[0] for home in all_homes]

#Scrape and create a list of links of the propertys
home_links = [home.find("a", class_="StyledPropertyCardDataArea-anchor")["href"] for home in all_homes]

driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfbNZxbADc3oNW-IvErNluBkuYUUC1Xo7nT_Ys49bDJvax0Ow/viewform?usp=dialog")

time.sleep(3)

for i in range(len(home_address)):

    # Address field
    address_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # Price field
    price_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # Link field
    link_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    #Send button
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address_field.send_keys(home_address[i])
    price_field.send_keys(home_prices[i])
    link_field.send_keys(home_links[i])
    time.sleep(1)
    submit_button.click()
    time.sleep(2)

    #Send another response button
    send_another_response_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_response_button.click()

    time.sleep(2)

driver.quit()