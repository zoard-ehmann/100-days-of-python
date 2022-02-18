import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


load_dotenv()

GOOGLE_FORM = os.getenv('SPREADSHEET')
ZILLOW_URL = os.getenv('ZILLOW')
ZILLOW_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'en-US,en;q=0.5'
}


driver = webdriver.Firefox(
    service=Service(
        executable_path=GeckoDriverManager(path='.wdm').install(),
        log_path=('.wdm/geckodriver.log')
    )
)
wait = WebDriverWait(driver=driver, timeout=15)

driver.get(ZILLOW_URL)

for i in range(10):
    time.sleep(.5)
    driver.find_element(By.ID, 'search-page-list-container').send_keys(Keys.PAGE_DOWN)

soup = BeautifulSoup(driver.page_source, 'html.parser')

cards = soup.select('.photo-cards > li')

rents = []
for card in cards:
    try:
        fetched_url = card.select_one('.list-card-link').attrs['href']

        if not fetched_url.startswith('https'):
            url = f'https://www.zillow.com{fetched_url}'
        else:
            url = fetched_url

        rents.append({
            'link': url,
            'price': card.select_one('.list-card-price').text,
            'address': card.select_one('.list-card-addr').text
        })
    except AttributeError:
        pass

driver.switch_to.new_window('tab')
driver.get(GOOGLE_FORM)

for flat in rents:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]//input'))).send_keys(flat['address'])
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]//input'))).send_keys(flat['price'])
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]//input'))).send_keys(flat['link'])
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.freebirdFormviewerViewNavigationLeftButtons div'))).click()
    time.sleep(.5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.freebirdFormviewerViewResponseLinksContainer a'))).click()

driver.quit()