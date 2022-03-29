import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def open_tab(driver, tag, namebutton):
    ActionChains(driver).click(driver.find_element(By.ID, tag)).perform()
    driver.implicitly_wait(time_to_wait=3)
    driver.switch_to.window(driver.window_handles[1])
    if not driver.switch_to.window(driver.window_handles[1]):
        time.sleep(0.5)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print(f"- Botón '{namebutton}' correcto")
        driver.implicitly_wait(time_to_wait=1)
    else:
        print(f"-- ¡¡¡ERROR!!! '{namebutton}' Button")


def browserWindows_flow(driver):
    print("--- TEST CASE: 'browserWindows' ---")
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element(By.ID, "close-fixedban").click()
    target = driver.find_element(By.XPATH,
                                 "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/div[2]")
    target.location_once_scrolled_into_view
    target.click()
    driver.find_element(By.XPATH,
                        "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]").click()

    #  -----------------------------------------------------------------------------------------

    open_tab(driver, "tabButton", 'New Tab')
    open_tab(driver, "windowButton", 'New Windows')
    open_tab(driver, "messageWindowButton", 'New Windows Message')

    print("--- TEST CASE Done ---")


class browserWindows_test:
    def __init__(self, driver):
        browserWindows_flow(driver)
