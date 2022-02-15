import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


load_dotenv()

LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
URL = 'https://www.linkedin.com/jobs/search?keywords=Python&location=Hungary&locationId=&geoId=100288700&f_TPR=&f_WT=2&position=1&pageNum=0'


def already_saved():
    try:
        driver.find_element(By.XPATH, '//span[text()="Saved"]')
        return True
    except NoSuchElementException:
        return False


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))
driver.get(URL)

cta_button = driver.find_element(By.LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'username').send_keys(LINKEDIN_USERNAME)
driver.find_element(By.ID, 'password').send_keys(LINKEDIN_PASSWORD)
driver.find_element(By.CSS_SELECTOR, '.login__form_action_container .btn__primary--large').click()
driver.find_element(By.XPATH, '//button[text()="Easy Apply"]').click()

time.sleep(3)

job_list = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list .jobs-search-results__list-item')

for job in job_list:
    job.click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'jobs-apply-button').click()

    try:
        driver.find_element(By.XPATH, '//span[text()="Submit application"]')
        save_job = True
    except NoSuchElementException:
        save_job = False
    finally:
        driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()
        driver.find_element(By.XPATH, '//span[text()="Discard"]').click()

        if save_job and not already_saved(): driver.find_element(By.XPATH, '//span[text()="Save"]').click()

driver.quit()