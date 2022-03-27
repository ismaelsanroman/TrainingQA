from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


def click_CheckBox(driver, tag):
    driver.find_element(By.XPATH, tag).click()


class checkBox_test:
    def __init__(self, driver):
        self.checkBox_flow(driver)

    def checkBox_flow(self, driver):
        print("--- TEST CASE: 'checkBox' ---")
        driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
        driver.find_element(By.ID, 'item-1').click()

        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]")
        driver.implicitly_wait(time_to_wait=3)
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]/button[1]/*[1]")
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[2]/span[1]/button[1]/*[1]")
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]/button[1]/*[1]")
        driver.implicitly_wait(time_to_wait=3)
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[2]/ol[1]/li[1]/span[1]/button[1]/*[1]")
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[2]/ol[1]/li[2]/span[1]/button[1]/*[1]")
        driver.implicitly_wait(time_to_wait=3)
        click_CheckBox(driver, "//span[contains(text(),'Excel File.doc')]")
        click_CheckBox(driver, "//span[contains(text(),'Word File.doc')]")
        click_CheckBox(driver, "//span[contains(text(),'General')]")
        click_CheckBox(driver, "//span[contains(text(),'Classified')]")
        click_CheckBox(driver, "//span[contains(text(),'Private')]")
        click_CheckBox(driver, "//span[contains(text(),'Public')]")
        click_CheckBox(driver, "//span[contains(text(),'Veu')]")
        click_CheckBox(driver, "//span[contains(text(),'Angular')]")
        click_CheckBox(driver, "//span[contains(text(),'React')]")
        click_CheckBox(driver, "//span[contains(text(),'Commands')]")
        click_CheckBox(driver, "//span[contains(text(),'Notes')]")
        driver.implicitly_wait(time_to_wait=3)

        # ----------------------------Titulos del desplegable------------------------------

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "rct-title"))
            )
        finally:
            print("-Revisión de los títulos del desplegable correcta")

        driver.implicitly_wait(time_to_wait=3)
        # ----------------------------Contar datos checkeados-----------------------------

        data_list = []
        data_class = driver.find_elements(By.CLASS_NAME, 'text-success')
        
        """for x in data_class:
            # print(x.text)
            data_list.append(x.text)"""

        if len(data_class) == 17:
            print("-Checkeo de checksbox correcto")
        else:
            print("---¡¡¡ERROR en el checkeo de checksbox!!!")

        driver.implicitly_wait(time_to_wait=3)

        # -----------------------------------------------------------------------------------

        click_CheckBox(driver, "//span[contains(text(),'Home')]")
        click_CheckBox(driver, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/*[1]")

        print("--- TEST CASE Done ---")

