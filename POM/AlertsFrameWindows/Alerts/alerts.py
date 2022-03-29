from selenium.webdriver.common.by import By
from datetime import time


def alerts_flow(driver):
    print("--- TEST CASE: 'alerts' ---")

    print("--- TEST CASE Done ---")


class alerts_test:
    def __init__(self, driver):
        alerts_flow(driver)
