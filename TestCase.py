from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import json
import time

with open('DataTesting/DataUser.json') as InfoUsu:
    UserData = json.load(InfoUsu)

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(0.5)
driver.get("https://demoqa.com/")
time.sleep(3)

driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()

driver.find_element(By.ID, 'item-0').click()

time.sleep(1)

driver.find_element(By.ID, 'userName').clear()
driver.find_element(By.ID, 'userName').send_keys(UserData['nombre'])

driver.find_element(By.ID, 'userEmail').clear()
driver.find_element(By.ID, 'userEmail').send_keys(UserData['email'])

driver.find_element(By.ID, 'currentAddress').clear()
driver.find_element(By.ID, 'currentAddress').send_keys(UserData['DirActual'])

driver.find_element(By.ID, 'permanentAddress').clear()
driver.find_element(By.ID, 'permanentAddress').send_keys(UserData['DirPermanent'])

InfoUsu.close()

driver.find_element(By.XPATH, "//button[@id='submit']").click()

# driver.find_element_by_id('name')
# driver.find_element_by_id('email')
# driver.find_element_by_xpath("//p[@id='currentAddress']")
# driver.find_element_by_xpath("//p[@id='permanentAddress']")

time.sleep(10)

# driver.close()
# driver.quit()
