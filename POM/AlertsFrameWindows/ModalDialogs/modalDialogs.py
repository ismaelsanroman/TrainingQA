from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


def open_button(driver, tag, close_id):
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, tag)))
    finally:
        ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
        time.sleep(1)
        num_car = len(driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]").text)
        ActionChains(driver).click(driver.find_element(By.ID, close_id)).perform()
        if num_car == 47 or num_car == 574:
            print(f"'Button {tag}' aceptado")
        else:
            print(f"-- ¡¡¡ERROR!!! 'Button {tag}'")

    driver.implicitly_wait(time_to_wait=3)


def modalDialogs_flow(driver):
    print("--- TEST CASE: 'modalDialogs' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[5]").click()

    #  -----------------------------------------------------------------------------------------

    open_button(driver, 'showSmallModal', "closeSmallModal")
    open_button(driver, 'showLargeModal', "closeLargeModal")

    time.sleep(3)

    print("--- TEST CASE Done ---")


class modalDialogs_test:
    def __init__(self, driver):
        modalDialogs_flow(driver)
