from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


AZ_URL = 'https://www.amazon.com/Wacom-Cintiq-Pro-Creative-Display/dp/B07BDDYK99/ref=sr_1_3?keywords=wacom+cintiq+pro+24&qid=1644561359&sprefix=wacom+cint%2Caps%2C174&sr=8-3'
PY_URL = 'https://python.org'


driver = webdriver.Firefox(service=Service(GeckoDriverManager(path='.wdm').install(), log_path='.wdm/geckodriver.log'))

# Get element by ID
# driver.get(AZ_URL)
# product = driver.find_element(By.ID, 'productTitle')
# print(product.text)

driver.get(PY_URL)
# Get element by name
# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute('placeholder'))

# Get element by class name
# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

# Get element by CSS selector
# doc_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(doc_link.text)

# Get element by XPath
# bug_link = driver.find_element(By.XPATH, '/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

#driver.close()
driver.quit()