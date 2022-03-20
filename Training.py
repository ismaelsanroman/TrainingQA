from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from POM.Elements.TextBox.textbox_test import textbox_test
from POM.Elements.CheckBox.checkBox_test import checkBox_test
from POM.Elements.RadioButtom.radioButtom_test import radioButtom_test
import unittest
import pytest
import json
import time
import os


class Training(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(8)
        driver.get("https://demoqa.com/")

    @pytest.mark.skipif(False)
    def test1_textBox(self):
        textbox_test(self.driver, user_data=self.get_json_data())

    @pytest.mark.skipif(False)
    def test2_checkBox(self):
        checkBox_test(self.driver, user_data=self.get_json_data())

    @pytest.mark.skipif(False)
    def test3_radioButtom(self):
        radioButtom_test(self.driver, user_data=self.get_json_data())


    @classmethod
    def tearDown(cls):
        print("\n FIN DE LOS TESTS")
        cls.driver.quit()


    @staticmethod
    def get_json_data():
        with open('DataTesting/DataUser.json') as InfoUsu:
            user_data = json.load(InfoUsu)
        return user_data


if __name__ == "__main__":
    #unittest.main(testRunner=HTMLTestRunner(output=os.getcwd(), report_title="Report by Isma"))
    unittest.main()

