from selenium.webdriver.common.by import By
import time


class brokenLinks_test:
    def __init__(self, driver):
        self.brokenLinks_flow(driver)

    def brokenLinks_flow(self, driver):
        print("--- TEST CASE: 'broken_links' ---")

        driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
        driver.find_element(By.ID, 'item-6').click()

        time.sleep(3)
        print("--- TEST CASE Done ---")