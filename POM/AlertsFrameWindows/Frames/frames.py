from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


def goto_frame(driver, tag, iframe):
    try:
        driver.switch_to.frame(iframe)
        # WebDriverWait(driver, 1).until(ec.driver.find_element(By.ID, tag))
        show_text = print(driver.find_element(By.ID, tag).text)
        print(f"'{iframe}' muestra el siguiente contenido: '{show_text}'")
        driver.switch_to.default_content()
    except TimeoutException:
        pass


def frames_flow(driver):
    print("--- TEST CASE: 'frames' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]").click()
    time.sleep(1)
    #  -----------------------------------------------------------------------------------------

    goto_frame(driver, 'sampleHeading', 'frame1')
    goto_frame(driver, 'sampleHeading', 'frame2')

    time.sleep(3)

    print("--- TEST CASE Done ---")


class frames_test:
    def __init__(self, driver):
        frames_flow(driver)
