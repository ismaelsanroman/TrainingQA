from datetime import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def insert_data(driver, tag, user_data):
    driver.find_element(By.ID, tag).clear()
    driver.find_element(By.ID, tag).send_keys(user_data)
    driver.implicitly_wait(time_to_wait=3)


def select_radio(driver, tag):
    driver.find_element(By.XPATH, tag).click()
    driver.implicitly_wait(time_to_wait=3)


def practiceForm_flow(driver, user_data):
    print("--- TEST CASE: 'practiceForm' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    target = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]").click()

    driver.find_element(By.XPATH, "//body/div[@id='fixedban']/div[1]/div[1]/a[1]/img[1]").click()

    insert_data(driver, 'firstName', user_data['nombre'])
    insert_data(driver, 'lastName', user_data['apellido'])
    insert_data(driver, 'userEmail', user_data['email'])

    # select_radio(driver, "//label[contains(text(),'Other')]")
    # select_radio(driver, "//label[contains(text(),'Female')]")
    # select_radio(driver, "//label[contains(text(),'Male')]")

    insert_data(driver, 'userNumber', user_data['numTelef'])

    # insert_data(driver, 'dateOfBirthInput', user_data['fchNacimiento'])
    # ActionChains(driver).click(driver.find_element(By.ID, 'dateOfBirthInput')).perform()

    # select_radio(driver, "//label[contains(text(),'Music')]")
    # select_radio(driver, "//label[contains(text(),'Reading')]")
    # select_radio(driver, "//label[contains(text(),'Sports')]")

    driver.find_element(By.ID, 'uploadPicture').send_keys("C:\\Users\\Ismael\\Downloads\\sampleFile.jpeg")
    print("- Imagen subida")

    insert_data(driver, 'currentAddress', user_data['DirActual'])

    # driver.find_element(By.ID, "state").select_by_value("")
    # driver.find_element(By.ID, "city").select_by_value("")

    p1 = ActionChains(driver).click(driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[10]/div[2]/div[1]/div[1]/div[1]")).perform()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    # ActionChains(driver).click(driver.find_element(By.CLASS_NAME, "")).perform()

    time.sleep(5)

    print("--- TEST CASE Done ---")


class practiceForm_test:
    def __init__(self, driver, user_data):
        practiceForm_flow(driver, user_data)
