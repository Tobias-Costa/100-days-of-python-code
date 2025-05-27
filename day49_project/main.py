import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
linkedin_email = os.environ["LINKEDIN_EMAIL"]
linkedin_password = os.environ["LINKEDIN_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4234493987&distance=25&f_AL=true&geoId=103836099&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

#Fazendo login no linkedin
time.sleep(5)

login_button = driver.find_element(by=By.CSS_SELECTOR, value=".sign-in-modal .sign-in-modal__outlet-btn")
login_button.click()

time.sleep(5)

email_input = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
email_input.send_keys(linkedin_email)

password_input = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
password_input.send_keys(linkedin_password)

submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".sign-in-form__submit-btn--full-width")
submit_button.click()

time.sleep(5)

# Salvando vagas de emprego
all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in all_jobs:
    job.click()
    print(job.text)
    time.sleep(2)
    try:
        save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
        time.sleep(3)
    except NoSuchElementException:
        continue

driver.quit()