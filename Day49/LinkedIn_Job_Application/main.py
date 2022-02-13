import os

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


load_dotenv()

LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
URL = 'https://www.linkedin.com/login?trk=homepage-basic_ispen-login-button'


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install(), log_path='Day49/LinkedIn_Job_Application/geckodriver.log'))
driver.get(URL)

mail_input = driver.find_element(By.ID, 'username')
pw_input = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container .btn__primary--large')

print(LINKEDIN_USERNAME)

mail_input.send_keys(LINKEDIN_USERNAME)
pw_input.send_keys(LINKEDIN_PASSWORD)
login_button.click()