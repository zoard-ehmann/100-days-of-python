import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager


load_dotenv()

TWITTER_EMAIL = os.getenv('TWITTER_MAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PW')
TWITTER_USERNAME = os.getenv('TWITTER_UN')
ISP = os.getenv('ISP_URL')


class InternetSpeedTwitterBot():
    
    def __init__(self):
        self.guaranteed_up: int
        self.guaranteed_down: int
        self.driver = webdriver.Firefox(
            service=Service(
                executable_path=GeckoDriverManager(path='.wdm').install(),
                log_path='.wdm/geckodriver.log'
            )
        )
        self.wait = WebDriverWait(driver=self.driver, timeout=120)
        self.__get_guaranteed_speed()

    def __get_guaranteed_speed(self):
        self.driver.get(ISP)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
        self.driver.find_element(By.CLASS_NAME, 'close').click()
        guaranteed_bw = self.driver.find_element(By.CLASS_NAME, 'field-name-field-garantalt-savszelesseg').text.split()[-2]
        self.guaranteed_down = int(guaranteed_bw.split('/')[0])
        self.guaranteed_up = int(guaranteed_bw.split('/')[1])

    def __populate_text_fields(self, text):
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'text')))
        self.driver.find_element(By.NAME, 'text').send_keys(text)
        self.driver.find_element(By.XPATH, '//span[text()="Next"]').click()

    def close_browser(self):
        self.driver.quit()

    def get_internet_speed(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get('https://www.speedtest.net')
        self.driver.find_element(By.ID, '_evidon-banner-acceptbutton').click()
        self.driver.find_element(By.CLASS_NAME, 'start-text').click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'result-data')))

        return {
            'up': float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text),
            'down': float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        }

    def tweet_at_provider(self, actual_speed):
        msg = f'Dear ISP! My internet speed is quite unsatisfying...\n\nGuaranteed: {self.guaranteed_down}/{self.guaranteed_up} Mb/s\nActual: {actual_speed["down"]}/{actual_speed["up"]} Mb/s'

        self.driver.switch_to.new_window('tab')
        self.driver.get('https://twitter.com')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Accept all cookies"]')))
        try:
            self.driver.find_element(By.XPATH, '//span[text()="Sign in"]').click()
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        
        self.__populate_text_fields(TWITTER_EMAIL)

        try:
            self.__populate_text_fields(TWITTER_USERNAME)
        except NoSuchElementException:
            pass

        self.wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
        self.driver.find_element(By.NAME, 'password').send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/compose/tweet"]')))
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/compose/tweet"]').click()
        self.driver.find_element(By.CLASS_NAME, 'public-DraftEditor-content').send_keys(msg)
        self.driver.find_element(By.XPATH, '//span[text()="Tweet"]').click()

