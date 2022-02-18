import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager


class InstaFollower():
    
    def __init__(self, firefox_profile: str=None):
        """Initialize Firefox webdriver and webdriver wait. If profile is passed, skips log in session - assumes you are already logged in.

        Args:
            firefox_profile (str, optional): Firefox profile to use. Defaults to None.
        """
        if firefox_profile == None:
            options = None
            self.skip_login = False
        else:
            options = Options()
            options.profile = firefox_profile
            self.skip_login = True

        self.driver = webdriver.Firefox(
            options=options,
            service=Service(
                executable_path=GeckoDriverManager(path='.wdm').install(),
                log_path='.wdm/geckodriver.log'
            )
        )

        self.wait = WebDriverWait(driver=self.driver, timeout=60)
        self.driver.get('https://www.instagram.com/')

    def __dismiss_prompt(self):
        """Dismisses Save Login and Turn On Notification prompts.
        """
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]'))).click()

    def end_session(self):
        """Quits from the browser.
        """
        self.driver.quit()

    def login(self, username: str, password: str):
        """Logs in to Instagram with the specified username and password combination.

        Args:
            username (str): Instagram username / phone number / email.
            password (str): Instagram password.
        """
        if not self.skip_login:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept All"]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password)

            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

            for _ in range(2):
                self.__dismiss_prompt()

    def find_followers(self, account: str):
        """Finds all the followers of the target account.

        Args:
            account (str): Name of the account whose followers has to be followed.
        """
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Search"]'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]').send_keys(account)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]'))).click()

    def follow(self):
        """Follows all the followers of the target account.
        """
        time.sleep(5)
        window = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        accounts = self.driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li')

        for account in accounts:
            try:
                button = account.find_element(By.CSS_SELECTOR, 'button div')
                if button.text == 'Follow':
                    button.click()
            except NoSuchElementException:
                pass
            
            time.sleep(5)
            window.send_keys(Keys.ARROW_DOWN)