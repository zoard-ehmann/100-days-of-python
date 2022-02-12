from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install(), log_path='Day48/Selenium_Webdriver/geckodriver.log'))
driver.get('https://www.amazon.com')
driver.quit()