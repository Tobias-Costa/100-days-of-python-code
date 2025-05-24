from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

timeout = time.time() + 60*5
buy_time = time.time() + 5

def find_most_expensive_update():
    
    all_updates = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
    expensive_update = all_updates[0]
    expensive_update_price = int(expensive_update.text.split("-")[1].strip().replace(",", ""))

    actual_cookies_number = int(driver.find_element(by=By.CSS_SELECTOR, value="#money").text)
    
    for update in all_updates:
        if update.text != "":
            update_price = int(update.text.split("-")[1].strip().replace(",", ""))
        else:
            update_price = 0
        
        if update_price > expensive_update_price and actual_cookies_number >= update_price:
            expensive_update = update
            expensive_update_price = update_price

    return expensive_update

while True:

    cookie.click()

    if time.time() > timeout:
        cookies_per_second = driver.find_element(by=By.CSS_SELECTOR, value="#cps")
        print(cookies_per_second.text)
        break
    elif time.time() > buy_time:
        expensive_update = find_most_expensive_update()
        expensive_update.click()
        buy_time = time.time() + 5

driver.quit()