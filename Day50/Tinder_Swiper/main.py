import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv


load_dotenv()

URL = 'https://tinder.com'
USERNAME = os.getenv('GOOGLE_UN')
PASSWORD = os.getenv('GOOGLE_PW')
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
wait = WebDriverWait(driver=driver, timeout=10)

wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]')))
driver.find_element(By.XPATH, '//span[text()="Log in"]').click()

tinder_window = driver.current_window_handle

time.sleep(1)
driver.find_element(By.XPATH, '//span[text()="Log in with Google"]').click()

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != tinder_window:
        driver.switch_to.window(window_name=window_handle)
        break

time.sleep(1)
driver.find_element(By.ID, 'identifierId').send_keys(USERNAME)
