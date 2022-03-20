from selenium.webdriver.common.by import By
import time

class textbox_test:
    def __init__(self, driver, user_data):
        self.textbox_flow(driver, user_data)

    def textbox_flow(self, driver, user_data):
        driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()

        driver.find_element(By.ID, 'item-0').click()

        time.sleep(1)

        driver.find_element(By.ID, 'userName').clear()
        driver.find_element(By.ID, 'userName').send_keys(user_data['nombre'])

        driver.find_element(By.ID, 'userEmail').clear()
        driver.find_element(By.ID, 'userEmail').send_keys(user_data['email'])

        driver.find_element(By.ID, 'currentAddress').clear()
        driver.find_element(By.ID, 'currentAddress').send_keys(user_data['DirActual'])

        driver.find_element(By.ID, 'permanentAddress').clear()
        driver.find_element(By.ID, 'permanentAddress').send_keys(user_data['DirPermanent'])

        driver.find_element(By.ID, 'submit').click()

        # driver.find_element_by_id('name')
        # driver.find_element_by_id('email')
        # driver.find_element_by_xpath("//p[@id='currentAddress']")
        # driver.find_element_by_xpath("//p[@id='permanentAddress']")