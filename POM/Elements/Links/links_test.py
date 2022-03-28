from selenium.webdriver.common.by import By


def click_link(driver, tag):
    driver.find_element(By.ID, tag).click()
    link_response = driver.find_element(By.ID, 'linkResponse')
    if link_response:
        print(f'- Enlace "{tag}" correcto')
        print("- Mensaje: ", link_response.text)
    else:
        print("Error en el encale ", tag)
    driver.implicitly_wait(time_to_wait=1)


def open_tab(driver, tag):
    driver.find_element(By.ID, tag).click()
    driver.implicitly_wait(time_to_wait=1)
    driver.switch_to.window(driver.window_handles[1])
    if driver.title == 'ToolsQA':
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print(f"- El enlace '{tag}' es correcto")
        driver.implicitly_wait(time_to_wait=1)
    else:
        print(f"-- ¡¡¡ERROR!!! con el enlace '{tag}'")


def links_flow(driver):
    print("--- TEST CASE: 'links' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-5').click()

    click_link(driver, 'created')
    click_link(driver, 'no-content')
    click_link(driver, 'moved')
    click_link(driver, 'bad-request')
    click_link(driver, 'unauthorized')
    click_link(driver, 'forbidden')
    click_link(driver, 'invalid-url')

    open_tab(driver, 'simpleLink')
    open_tab(driver, 'dynamicLink')

    print("--- TEST CASE Done ---")


class links_test:
    def __init__(self, driver):
        links_flow(driver)
