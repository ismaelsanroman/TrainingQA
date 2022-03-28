import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def verify_UpDown(driver):
    file_path = driver.find_element(By.ID, 'uploadedFilePath').text
    if file_path:
        print("- Descarga y subida del archivo correcta")
    else:
        print("-- ¡¡¡ERROR!!! en la descarga y subida del archivo")

def uploadDownload_flow(driver):
    print("--- TEST CASE: 'uploadDownload' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    target = driver.find_element(By.ID, 'item-7')
    target.location_once_scrolled_into_view
    target.click()

    ActionChains(driver).click(driver.find_element(By.ID, 'downloadButton')).perform()
    time.sleep(4)

    driver.find_element(By.ID, 'uploadFile').send_keys("C:\\Users\\Ismael\\Downloads\\sampleFile.jpeg")
    verify_UpDown(driver)

    print("--- TEST CASE Done ---")


class uploadDownload_test:
    def __init__(self, driver):
        uploadDownload_flow(driver)

