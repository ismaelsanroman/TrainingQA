from selenium.webdriver.common.by import By
import time


def bookStore_flow(driver):
    print("--- TEST CASE: 'bookStore' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH,
                        "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/ul[1]/li[2]").click()

    #  -----------------------------------------------------------------------------------------
    time.sleep(3)

    print("--- TEST CASE Done ---")


class bookStore_test:
    def __init__(self, driver):
        bookStore_flow(driver)
