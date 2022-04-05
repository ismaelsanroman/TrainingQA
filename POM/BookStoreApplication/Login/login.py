from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time


def login(driver, user, password, nombre, apellido):
    print("")
    driver.find_element(By.ID, 'userName').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login').click()
    print("Message: ", driver.find_element(By.ID, 'name').text)

    ActionChains(driver).click(driver.find_element(By.ID, 'newUser')).perform()

    driver.find_element(By.ID, 'firstname').send_keys(nombre)
    driver.find_element(By.ID, 'lastname').send_keys(apellido)
    driver.find_element(By.ID, 'userName').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)

    ActionChains(driver).click(driver.find_element(By.XPATH,
                                                   "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[3]")).perform()
    # print("Message: ", driver.find_element(By.ID, 'name').text)


def login_flow(driver, user_data):
    print("--- TEST CASE: 'login' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.XPATH, "//body/div[@id='fixedban']/div[1]/div[1]/a[1]/img[1]").click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]").click()
    target = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    time.sleep(0.5)
    """wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable(target))"""
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/ul[1]/li[1]").click()

    #  -----------------------------------------------------------------------------------------

    login(driver, user_data['user'], user_data['password'], user_data['nombre'], user_data['apellido'])

    time.sleep(3)

    print("--- TEST CASE Done ---")


class login_test:
    def __init__(self, driver, user_data):
        login_flow(driver, user_data)
