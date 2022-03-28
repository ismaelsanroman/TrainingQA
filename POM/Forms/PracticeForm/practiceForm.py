from selenium.webdriver.common.by import By
import time


def insert_data(driver, tag, user_data):
    driver.find_element(By.ID, tag).clear()
    driver.find_element(By.ID, tag).send_keys(user_data)


def practiceForm_flow(driver):
    print("--- TEST CASE: 'practiceForm' ---")
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    target = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]") \
        .click()

    time.sleep(3)

    print("--- TEST CASE Done ---")


class practiceForm_test:
    def __init__(self, driver):
        practiceForm_flow(driver)
