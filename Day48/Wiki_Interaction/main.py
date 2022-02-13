from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


WIKI_URL = 'https://en.wikipedia.org/wiki/Main_Page'


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install(), log_path='Day48/Wiki_Interaction/geckodriver.log'))
driver.get(WIKI_URL)

articles = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
print(articles.text)

driver.quit()