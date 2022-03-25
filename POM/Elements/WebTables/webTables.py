from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def verify_value(driver, value):
    Select(driver.find_element(By.XPATH,
                               "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div["
                               "2]/span[2]/select[1]")).select_by_value(value)

    count_row = driver.find_elements(By.CLASS_NAME, 'rt-tr-group')
    print(len(count_row), "Correct")

    driver.implicitly_wait(3)


class webTables_test:
    def __init__(self, driver, user_data):
        self.webTables_flow(driver, user_data)

    def webTables_flow(self, driver, user_data):
        print("--- TEST CASE: 'webTables' ---")
        driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
        driver.find_element(By.ID, 'item-3').click()

        verify_value(driver, '5')
        verify_value(driver, '10')
        verify_value(driver, '20')
        verify_value(driver, '25')
        verify_value(driver, '50')
        verify_value(driver, '100')

        time.sleep(3)

        print("--- TEST CASE Done ---")