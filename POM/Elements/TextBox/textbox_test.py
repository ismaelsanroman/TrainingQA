from selenium.webdriver.common.by import By
import time

class textbox_test:
    def __init__(self, driver, user_data):
        self.textbox_flow(driver, user_data)

    def textbox_flow(self, driver, user_data):
        driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
        driver.find_element(By.ID, 'item-0').click()
        self.clear_and_sendkeys(driver, 'userName', user_data['nombre'])
        self.clear_and_sendkeys(driver, 'userEmail', user_data['email'])
        self.clear_and_sendkeys(driver, 'currentAddress', user_data['DirActual'])
        self.clear_and_sendkeys(driver, 'permanentAddress', user_data['DirPermanent'])
        driver.find_element(By.ID, 'submit').click()

        # driver.find_element_by_id('name')
        # driver.find_element_by_id('email')
        # driver.find_element_by_xpath("//p[@id='currentAddress']")
        # driver.find_element_by_xpath("//p[@id='permanentAddress']")

    def clear_and_sendkeys(self, driver, tag, user_data):
        driver.find_element(By.ID, tag).clear()
        driver.find_element(By.ID, tag).send_keys(user_data)