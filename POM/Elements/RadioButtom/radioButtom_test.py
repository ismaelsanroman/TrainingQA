from selenium.webdriver.common.by import By


def verify_radioButtom(driver, tag_xpath, tag_css, tag_name):
    buttom_xpath = driver.find_element(By.XPATH, tag_xpath)
    buttom_css = driver.find_element(By.CSS_SELECTOR, tag_css).is_displayed()

    if not buttom_css:
        print("- Está disponible para su selección")
        if not buttom_xpath.is_selected():
            if not buttom_xpath.is_selected():
                buttom_xpath.click()

        else:
            print("- No es válido para seleccionar")
    else:
        print("- No está disponible para su selección")

    if driver.find_element(By.CLASS_NAME, "text-success").text == buttom_xpath.text:
        print("- RadioButtom, '" + tag_name + "' Seleccionado")
    else:
        print("--- ¡¡¡ERROR RadioButtom '" + tag_name + "'!!!")

    driver.implicitly_wait(3)


def radioButtom_flow(driver):
    print("--- TEST CASE: 'radioButtom' ---")
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-2').click()
    driver.implicitly_wait(1)

    # ---------------------------------------------------------------------------------------

    verify_radioButtom(driver, "//label[contains(text(),'Yes')]", "input[id='yesRadio']", "Yes")

    verify_radioButtom(driver, "//label[contains(text(),'Impressive')]", "input[id='impressiveRadio']", "Impressive")

    verify_radioButtom(driver, "//label[contains(text(),'No')]", "input[id='noRadio']", "No")

    # --------------------------------------------------------------------------------------

    print("--- TEST CASE Done ---")


class radioButtom_test:
    def __init__(self, driver):
        radioButtom_flow(driver)
