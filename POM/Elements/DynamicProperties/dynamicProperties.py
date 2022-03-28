from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


def dynamicProperties_flow(driver):
    print("--- TEST CASE: 'dynamicProperties' ---")
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    target = driver.find_element(By.ID, 'item-8')
    target.location_once_scrolled_into_view
    target.click()

    try:
        WebDriverWait(driver, 6).until(
            ec.element_to_be_clickable((By.ID, 'enableAfter')))
        print("- Elemento clicable")
    finally:

        try:
            WebDriverWait(driver, 6).until(
                ec.element_to_be_clickable((By.CLASS_NAME, "text-danger")))
            print("- Color del boton modificado")
        finally:

            try:
                WebDriverWait(driver, 6).until(
                    ec.presence_of_element_located((By.ID, 'visibleAfter')))
                print("- Elemento visible")
            finally:
                print("")

    print("--- TEST CASE Done ---")


class dynamicProperties_test:
    def __init__(self, driver):
        dynamicProperties_flow(driver)