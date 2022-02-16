import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


load_dotenv()

URL = 'https://tinder.com'
PROFILE = os.getenv('FIREFOX_PROFILE')


options = Options()
options.profile = PROFILE
driver = webdriver.Firefox(
    options=options,
    service=Service(
        executable_path=GeckoDriverManager(path='.wdm').install(),
        log_path='.wdm/geckodriver.log',
    ),
)
driver.get(URL)
wait = WebDriverWait(driver=driver, timeout=60)

wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Personalize My Choices"]')))
driver.find_element(By.XPATH, '//span[text()="Personalize My Choices"]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Refuse All"]')))
driver.find_element(By.XPATH, '//span[text()="Refuse All"]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[contains(@class, "Isolate")]/div/div[2]/button')))

while True:
    main_page = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[contains(@class, "Isolate")]/div/div[2]/button').click()
    time.sleep(3)
