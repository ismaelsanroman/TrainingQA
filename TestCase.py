from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
import time

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
driver.find_element_by_id('userName').send_keys('Ismael')
driver.find_element_by_id('userEmail').clear()
driver.find_element_by_id('userEmail').send_keys('ismaelsanromansanchez@gmail.com')
driver.find_element_by_id('currentAddress').clear()
driver.find_element_by_id('currentAddress').send_keys('C/ República de Ecuador, '
                                                      '6, 3º Izda, 06011, '
                                                      'Badajoz (Badajoz)')
driver.find_element_by_id('permanentAddress').clear()
driver.find_element_by_id('permanentAddress').send_keys('C/ Molino de San Jerónimo, '
                                                        '23, bajo, 10140, '
                                                        'Guadalupe (Cáceres)')

driver.find_element_by_id("submit").click()

# Name:Ismael
# Email:ismaelsanromansanchez@gmail.com
# Current Address :C/ República de Ecuador, 6, 3º Izda, 06011, Badajoz (Badajoz)
# Permananet Address :C/ Molino de San Jerónimo, 23, bajo, 10140, Guadalupe (Cáceres)

time.sleep(10)

# driver.close()
# driver.quit()
