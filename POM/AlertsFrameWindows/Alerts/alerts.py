from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


def button_wait(driver, tag):
    try:
        open_button(driver, tag)
        WebDriverWait(driver, 6).until(ec.alert_is_present())
        Alert(driver).accept()
        print("Boton 'Click me' aceptado")
    except TimeoutException:
        pass


def button_dismiss(driver, tag):
    try:
        ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
        WebDriverWait(driver, 1).until(ec.alert_is_present())
        Alert(driver).dismiss()
        if not print(driver.find_element(By.ID, 'confirmResult').text) == 'You selected Cancel':
            print("- 'Confirm Box' es correcto")
        else:
            print("-- ¡¡¡ERROR!!! en 'Confirm Box'")
    except TimeoutException:
        pass


def button_acept(driver, tag):
    try:
        ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
        WebDriverWait(driver, 1).until(ec.alert_is_present())
        Alert(driver).accept()
        if not print(driver.find_element(By.ID, 'confirmResult').text) == 'You selected Ok':
            print("- 'Confirm Box' es correcto")
        else:
            print("-- ¡¡¡ERROR!!! en 'Confirm Box'")
    except TimeoutException:
        pass


def open_button(driver, tag):
    try:
        ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
        WebDriverWait(driver, 1).until(ec.alert_is_present())
        Alert(driver).accept()
        print("'Click Button' aceptado")
        driver.implicitly_wait(time_to_wait=3)
    except TimeoutException:
        pass


def button_prompt(driver, tag, name):
    try:
        ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
        WebDriverWait(driver, 1).until(ec.alert_is_present())
        Alert(driver).send_keys(name)
        Alert(driver).accept()

        if not print(driver.find_element(By.ID, 'promptResult').text) == name:
            print("- 'Prompt Box' es correcto")
        else:
            print("-- ¡¡¡ERROR!!! en 'Prompt Box'")
    except TimeoutException:
        pass


def alerts_flow(driver):
    print("--- TEST CASE: 'alerts' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH,
                        "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]").click()

    #  -----------------------------------------------------------------------------------------

    open_button(driver, 'alertButton')

    button_wait(driver, 'timerAlertButton')

    button_acept(driver, 'confirmButton')
    button_dismiss(driver, 'confirmButton')

    button_prompt(driver, 'promtButton', "Ismael Sanroman")

    time.sleep(3)

    print("--- TEST CASE Done ---")


class alerts_test:
    def __init__(self, driver):
        alerts_flow(driver)
