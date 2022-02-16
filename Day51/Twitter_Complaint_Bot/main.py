import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


load_dotenv()

TWITTER_USERNAME = os.getenv('TWITTER_UN')
TWITTER_PASSWORD = os.getenv('TWITTER_PW')

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))
wait = WebDriverWait(driver=driver, timeout=15)

driver.get('https://twitter.com')

driver.switch_to.new_window('tab')
driver.get('https://digi.hu/ajanlat/internet/lan')

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
driver.find_element(By.CLASS_NAME, 'close').click()

guaranteed_bw = driver.find_element(By.CLASS_NAME, 'field-name-field-garantalt-savszelesseg').text.split()[-2]
guaranteed_down = guaranteed_bw.split('/')[0]
guaranteed_up = guaranteed_bw.split('/')[1]
