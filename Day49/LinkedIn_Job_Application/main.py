import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


load_dotenv()

LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
URL = 'https://www.linkedin.com/jobs/search?keywords=Python&location=Hungary&locationId=&geoId=100288700&f_TPR=&f_WT=2&position=1&pageNum=0'


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))
driver.get(URL)

cta_button = driver.find_element(By.LINK_TEXT, 'Sign in')
cta_button.click()

mail_input = driver.find_element(By.ID, 'username')
mail_input.send_keys(LINKEDIN_USERNAME)

pw_input = driver.find_element(By.ID, 'password')
pw_input.send_keys(LINKEDIN_PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container .btn__primary--large')
login_button.click()

easy_apply = driver.find_element(By.XPATH, '//button[text()="Easy Apply"]')
easy_apply.click()

time.sleep(3)

first_job = driver.find_element(By.CSS_SELECTOR, '.jobs-search-results__list li')
first_job.click()

save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
save_button.click()