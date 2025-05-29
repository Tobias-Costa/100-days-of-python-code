import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

PROMISED_DOWN = 200
PROMISED_UP = 200

class InternetSpeedXBot:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0
        self._x_email = os.environ["X_EMAIL"]
        self._x_password = os.environ["X_PASSWORD"]

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        # Accept privacy policy terms
        privacy_policy_button = self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
        privacy_policy_button.click()

        time.sleep(1)

        # Starting Internet test
        start_test_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        start_test_button.click()

        time.sleep(60)

        self.down = float(self.driver.find_element(by=By.CSS_SELECTOR, value=".result-data .download-speed").text)
        self.up = float(self.driver.find_element(by=By.CSS_SELECTOR, value=".result-data .upload-speed").text)

        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):

        #Login

        self.driver.get("https://x.com/login")

        time.sleep(3)

        login_email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        login_email.send_keys(self._x_email)

        login_email_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        login_email_button.click()

        time.sleep(2)

        try:

            password_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(self._x_password) 

            login_password_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            login_password_button.click()

        except NoSuchElementException:

            username_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input')
            username_input.send_keys(os.environ["X_USERNAME"], Keys.ENTER)                                             

            time.sleep(1)

            password_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(self._x_password)

            login_password_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            login_password_button.click()

        #Tweeting

        time.sleep(5)

        x_compose = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        x_msg = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        x_compose.send_keys(x_msg)

        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()

        self.driver.quit()