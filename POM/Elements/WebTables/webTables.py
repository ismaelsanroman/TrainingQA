from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def insert_data(driver, tag, user_data):
    driver.find_element(By.ID, tag).clear()
    driver.find_element(By.ID, tag).send_keys(user_data)
    driver.implicitly_wait(3)


def find_user(driver, name_user):
    driver.find_element(By.ID, 'searchBox').clear()
    driver.find_element(By.ID, 'searchBox').send_keys(name_user)
    driver.find_element(By.ID, 'searchBox').clear()
    driver.refresh()
    driver.implicitly_wait(3)


def verify_value(driver):
    for n in ["100", "50", "25", "20", "10", "5"]:
        Select(driver.find_element(By.XPATH,
                                    "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div["
                                    "2]/span[2]/select[1]")).select_by_value(n)
        count_row = driver.find_elements(By.CLASS_NAME, 'rt-tr-group')
        print("- Lista de ", len(count_row), " Correcta")

        driver.implicitly_wait(3)


def delete_user(driver):
    for n in [1, 2, 3]:
        driver.find_element(By.CSS_SELECTOR, f"#delete-record-{n}").click()
        driver.implicitly_wait(3)
    print("-- Usuarios eliminados")


def webTables_flow(driver, user_data):
    print("--- TEST CASE: 'webTables' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-3').click()
    verify_value(driver)
    find_user(driver, 'Pepe')
    delete_user(driver)
    driver.find_element(By.ID, 'addNewRecordButton').click()

    insert_data(driver, 'firstName', user_data['nombre'])
    insert_data(driver, 'lastName', user_data['apellido'])
    insert_data(driver, 'userEmail', user_data['email'])
    insert_data(driver, 'age', user_data['edad'])
    insert_data(driver, 'salary', user_data['salario'])
    insert_data(driver, 'department', user_data['profesion'])

    driver.find_element(By.ID, 'submit').click()

    #  Assertion
    element = driver.find_element(By.XPATH, f"// div[contains(text(), '{user_data['nombre']}')]")
    assert element.text == user_data['nombre']

    print("--- TEST CASE Done ---")


class webTables_test:
    def __init__(self, driver, user_data):
        webTables_flow(driver, user_data)
