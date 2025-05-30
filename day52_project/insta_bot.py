import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.action =  ActionChains(self.driver)
        self.similar_account = "waldir.dev"
        self._username = os.environ["INSTA_USERNAME"]
        self._password = os.environ["INSTA_PASSWORD"]

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)

        username_input = self.driver.find_element(by=By.NAME, value="username")
        username_input.send_keys(self._username)

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(self._password, Keys.ENTER)

        time.sleep(6)

    def find_followers(self):

        self.driver.get(f"https://www.instagram.com/{self.similar_account}/")

        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value='//*[contains(text(), "seguidores")]').click()

        time.sleep(5)

    def follow(self):
            
        followers = self.driver.find_elements(by=By.XPATH, value='//*[contains(text(), "Seguir")]')

        for follower in followers:

            if follower == followers[-1]:
                time.sleep(1)
                scroll_origin = ScrollOrigin.from_element(follower)
                self.action.scroll_from_origin(scroll_origin, 0, 200).click(follower).perform()
            else:
                time.sleep(1)
                self.action.scroll_to_element(follower).click(follower).perform()

            try:
                time.sleep(1)
                self.driver.find_element(by=By.XPATH, value='//button[contains(text(), "OK")]').click()
            except NoSuchElementException:
                continue