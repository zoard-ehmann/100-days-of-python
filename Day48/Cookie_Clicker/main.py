import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


URL = 'https://orteil.dashnet.org/experiments/cookie/'


def set_timestamp():
    return time.time()


def runtime():
    global last_timestamp
    current_timestamp = set_timestamp()
    if current_timestamp - last_timestamp >= 5:
        last_timestamp = set_timestamp()
        return True
    return False


def check_store():
    money = int(driver.find_element(By.ID, 'money').text)
    addons = driver.find_elements(By.CSS_SELECTOR, '#store div b')
    addons = addons[::-1]
    for add in addons:
        try:
            if money > int(add.text.split('-')[1].replace(',', '')):
                add.click()
                break
        except IndexError:
            pass


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))
driver.get(URL)

cookie = driver.find_element(By.ID, 'cookie')

expected_finish = set_timestamp() + 5 * 60
last_timestamp = set_timestamp()

while True:
    cookie.click()
    if runtime():
        check_store()

    if set_timestamp() >= expected_finish:
        cps = driver.find_element(By.ID, 'cps').text
        print(f'5 minutes have passed.\n{cps}')
        break
