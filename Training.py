from selenium import webdriver
import unittest
import pytest
import json
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

from POM.Elements.TextBox.textbox_test import textbox_test
from POM.Elements.CheckBox.checkBox_test import checkBox_test
from POM.Elements.RadioButtom.radioButtom_test import radioButtom_test
from POM.Elements.WebTables.webTables import webTables_test
from POM.Elements.Button.button_test import button_test


class Training(unittest.TestCase):

    """
    @classmethod
    def setUpClass(cls):
    """

    @classmethod
    def setUp(cls):
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://demoqa.com/")
        driver.implicitly_wait(time_to_wait=10)
    """
    @pytest.mark.skipif(False)
    def test1_textBox(self):
        textbox_test(self.driver, user_data=self.get_json_data())

    @pytest.mark.skipif(True)
    def test2_checkBox(self):
        checkBox_test(self.driver)

    @pytest.mark.skipif(False)
    def test3_radioButtom(self):
        radioButtom_test(self.driver)
    
    @pytest.mark.skipif(False)
    def test4_webTables(self):
        webTables_test(self.driver, user_data=self.get_json_data())
    """

    @pytest.mark.skipif(True)
    def test5_button(self):
        button_test(self.driver)

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
    # unittest.main(testRunner=HTMLTestRunner(output=os.getcwd(), report_title="Report by Ismael"))
    unittest.main()