from selenium.webdriver.common.by import By


def clear_and_sendkeys(driver, tag, user_data):
    driver.find_element(By.ID, tag).clear()
    driver.find_element(By.ID, tag).send_keys(user_data)


def textbox_flow(driver, user_data):
    print("--- TEST CASE: 'testBox' ---")
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-0').click()
    clear_and_sendkeys(driver, 'userName', user_data['nombre'])
    clear_and_sendkeys(driver, 'userEmail', user_data['email'])
    clear_and_sendkeys(driver, 'currentAddress', user_data['DirActual'])
    clear_and_sendkeys(driver, 'permanentAddress', user_data['DirPermanent'])
    driver.find_element(By.ID, 'submit').click()

    # -------------------------------------------------------------------------------------------------------

    obt_nombre = driver.find_element(By.ID, 'name').text
    obt_email = driver.find_element(By.ID, 'email').text
    obt_diractual = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
    obt_midir = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

    if obt_nombre == "Name:" + user_data['nombre'] \
            and obt_email == "Email:" + user_data['email'] \
            and obt_diractual == "Current Address :" + user_data['DirActual'] \
            and obt_midir == "Permananet Address :" + user_data['DirPermanent']:
        print("Obtención de datos CORRECTA")
    else:
        print("¡ERROR! Los datos introducidos no concuerdan con los obtenidos.")

    print("--- TEST CASE Done ---")


class textbox_test:
    def __init__(self, driver, user_data):
        textbox_flow(driver, user_data)

