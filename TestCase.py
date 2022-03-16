from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
import json
import time

with open('DataTesting/DataUser.json') as InfoUsu:
    UserData = json.load(InfoUsu)

# print(UserData[0])

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(0.5)
driver.get("https://demoqa.com/")

# driver.find_elements(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]') # Revisar con JA
driver.find_element_by_xpath('//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
driver.find_element_by_id('item-0').click()
time.sleep(1)
driver.find_element_by_id('userName').clear()
driver.find_element_by_id('userName').send_keys(UserData['nombre'])
driver.find_element_by_id('userEmail').clear()
driver.find_element_by_id('userEmail').send_keys(UserData['email'])
driver.find_element_by_id('currentAddress').clear()
driver.find_element_by_id('currentAddress').send_keys(UserData['DirActual'])
driver.find_element_by_id('permanentAddress').clear()
driver.find_element_by_id('permanentAddress').send_keys(UserData['DirPermanente'])

InfoUsu.close()

# driver.find_element_by_id("submit").submit()

driver.find_element_by_id('name')
driver.find_element_by_id('email')
driver.find_element_by_xpath("//p[@id='currentAddress']")
driver.find_element_by_xpath("//p[@id='permanentAddress']")

time.sleep(10)

# driver.close()
# driver.quit()
