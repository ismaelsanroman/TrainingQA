from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.delete_all_cookies()

driver.timeouts.page_load
driver.timeouts.implicit_wait

driver.get("https://demoqa.com/")

time.sleep(3)

driver.find_elements(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]')

time.sleep(5)

driver.close()
driver.quit()
