from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time


def nestedFrames_flow(driver):
    print("--- TEST CASE: 'nestedFrames' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[4]").click()

    #  -----------------------------------------------------------------------------------------
    time.sleep(0.5)
    try:
        driver.switch_to.frame('frame1')
        tag1 = driver.find_element(By.TAG_NAME, "body").text
        print("- Iframe parent con el contenido: ", tag1)

        driver.switch_to.frame(0)
        tag2 = driver.find_element(By.TAG_NAME, "p").text
        print("- Iframe child con el contenido: ", tag2)
    except TimeoutException:
        pass

    print("--- TEST CASE Done ---")


class nestedFrames_test:
    def __init__(self, driver):
        nestedFrames_flow(driver)
