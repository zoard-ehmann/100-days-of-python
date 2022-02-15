import pprint

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


PY_URL = 'https://python.org'


pp = pprint.PrettyPrinter()
driver = webdriver.Firefox(service=Service(GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))

driver.get(PY_URL)

event_menu = driver.find_element(By.CSS_SELECTOR, '.event-widget .menu')
event_dates = event_menu.find_elements(By.TAG_NAME, 'time')
event_names = event_menu.find_elements(By.TAG_NAME, 'a')

upcoming_events = {
    nr: {
        'time':event_dates[nr].text,
        'name':event_names[nr].text
    } for nr in range(len(event_names))
}

pp.pprint(upcoming_events)

driver.quit()