from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


URL = 'http://secure-retreat-92358.herokuapp.com/'


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install(), log_path='Day48/Automatic_Sign_Up/geckodriver.log'))
driver.get(URL)

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Zoard')

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Ehmann')

email = driver.find_element(By.NAME, 'email')
email.send_keys('zoard@mail.com')

# Sign up by pressing ENTER
# email.send_keys(Keys.ENTER)

# Sign up by clicking on button
sign_up = driver.find_element(By.CLASS_NAME, 'btn')
sign_up.click()