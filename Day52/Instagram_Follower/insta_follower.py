import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class InstaFollower():
    
    def __init__(self):
        """Initialize Firefox webdriver and webdriver wait.
        """
        self.driver = webdriver.Firefox(
            service=Service(
                executable_path=GeckoDriverManager(path='.wdm').install(),
                log_path='.wdm/geckodriver.log'
            )
        )
        self.wait = WebDriverWait(driver=self.driver, timeout=60)

    def __dismiss_prompt(self):
        """Dismisses Save Login and Turn On Notification prompts.
        """
        save_login = '//button[text()="Not Now"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, save_login)))
        self.driver.find_element(By.XPATH, save_login).click()

    def login(self, username: str, password: str):
        """Logs in to Instagram with the specified username and password combination.

        Args:
            username (str): Instagram username / phone number / email.
            password (str): Instagram password.
        """
        self.driver.get('https://www.instagram.com/')

        cookie_accept = '//button[text()="Accept All"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, cookie_accept)))
        self.driver.find_element(By.XPATH, cookie_accept).click()

        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)

        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        for _ in range(2):
            self.__dismiss_prompt()

    def find_followers(self):
        pass

    def follow(self):
        pass