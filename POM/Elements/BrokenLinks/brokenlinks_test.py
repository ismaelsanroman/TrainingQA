from selenium.webdriver.common.by import By


def click_link(driver, tag):
    driver.find_element(By.XPATH, tag).click()
    if driver.title == 'ToolsQA':
        print('Enlace correcto')
    else:
        print('-- ¡¡¡ERROR!!! Enlace incorrecto')
    driver.back()
    driver.implicitly_wait(time_to_wait=1)


def img_verify(driver, tag):
    img = driver.find_element(By.XPATH, tag)
    width = img.get_attribute("width")
    height = img.get_attribute("height")
    if width != "0" and height != "0":
        print('- Imagen insertada correctamente')
    else:
        print('-- ¡¡¡ERROR!!! Imagen incorrecta')


def brokenLinks_flow(driver):
    print("--- TEST CASE: 'broken_links' ---")

    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, 'item-6').click()

    img_verify(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/img[1]")
    img_verify(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/img[2]")

    click_link(driver, "//a[contains(text(),'Click Here for Valid Link')]")
    click_link(driver, "//a[contains(text(),'Click Here for Broken Link')]")

    print("--- TEST CASE Done ---")


class brokenLinks_test:
    def __init__(self, driver):
        brokenLinks_flow(driver)
