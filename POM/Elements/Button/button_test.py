from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def button_flow(driver):
    print("--- TEST CASE: 'button' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-4').click()

    ActionChains(driver).double_click(driver.find_element(By.ID, 'doubleClickBtn')).perform()
    ActionChains(driver).context_click(driver.find_element(By.ID, 'rightClickBtn')).perform()
    ActionChains(driver).click(driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div["
                                                            "2]/div[2]/div[3]/button[1]")).perform()

    doubleClickMessage = driver.find_element(By.ID, 'doubleClickMessage').text
    rightClickMessage = driver.find_element(By.ID, 'rightClickMessage').text
    dynamicClickMessage = driver.find_element(By.ID, 'dynamicClickMessage').text

    if doubleClickMessage != 'You have done a double click':
        print("Error al clicar el botón 'Double Click Me'")
    elif rightClickMessage != 'You have done a right click':
        print("Error al clicar el botón 'Right Click Me'")
    elif dynamicClickMessage != 'You have done a dynamic click':
        print(" -Error al clicar el botón 'Click Me'")
    else:
        print("- Botones clicados correctamente")

    print("--- TEST CASE Done ---")


class button_test:
    def __init__(self, driver):
        button_flow(driver)

