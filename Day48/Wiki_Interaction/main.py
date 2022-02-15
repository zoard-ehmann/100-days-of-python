from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


WIKI_URL = 'https://en.wikipedia.org/wiki/Main_Page'


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))
driver.get(WIKI_URL)

articles = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
#articles.click()

all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)