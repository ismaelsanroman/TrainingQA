from selenium import webdriver
import unittest
import pytest
import json
import os

from behave import *

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

from POM.API.Api import api_test
from POM.Elements.TextBox.textbox_test import textbox_test
from POM.Elements.CheckBox.checkBox_test import checkBox_test
from POM.Elements.RadioButtom.radioButtom_test import radioButtom_test
from POM.Elements.WebTables.webTables import webTables_test
from POM.Elements.Button.button_test import button_test
from POM.Elements.Links.links_test import links_test
from POM.Elements.BrokenLinks.brokenlinks_test import brokenLinks_test
from POM.Elements.UploadDownload.uploadDownload import uploadDownload_test
from POM.Elements.DynamicProperties.dynamicProperties import dynamicProperties_test
from POM.Forms.PracticeForm.practiceForm import practiceForm_test
from POM.AlertsFrameWindows.Alerts.alerts import alerts_test
from POM.AlertsFrameWindows.BrowserWindows.browserWindows import browserWindows_test
from POM.AlertsFrameWindows.Frames.frames import frames_test
from POM.AlertsFrameWindows.ModalDialogs.modalDialogs import modalDialogs_test
from POM.AlertsFrameWindows.NestedFrames.nestedFrames import nestedFrames_test
from POM.BookStoreApplication.BookStore.bookStore import bookStore_test
from POM.BookStoreApplication.Login.login import login_test
from POM.BookStoreApplication.Profile.profile import profile_test

"""
@given('we have behave installed')
@when('we implement a test')
@then('behave will test it for us!')
"""


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
    @given(u'I load the website')
    def test1_textBox(self):
        textbox_test(self.driver, user_data=self.get_json_data())

    
    @pytest.mark.skipif(False)
    def test2_checkBox(self):
        checkBox_test(self.driver)

    @pytest.mark.skipif(False)
    def test3_radioButtom(self):
        radioButtom_test(self.driver)

    @pytest.mark.skipif(False)
    def test4_webTables(self):
        webTables_test(self.driver, user_data=self.get_json_data())

    @pytest.mark.skipif(False)
    def test5_button(self):
        button_test(self.driver)

    @pytest.mark.skipif(False)
    def test6_links(self):
        links_test(self.driver)

    @pytest.mark.skipif(False)
    def test7_brokenLinks(self):
        brokenLinks_test(self.driver)

    @pytest.mark.skipif(False)
    def test8_uploadDownload(self):
        uploadDownload_test(self.driver)

    @pytest.mark.skipif(False)
    def test9_dynamicProperties(self):
        dynamicProperties_test(self.driver)
    
    @pytest.mark.skipif(False) # ---> Sin terminar
    def test10_practiceForm(self):
        practiceForm_test(self.driver, user_data=self.get_json_data())
    
    @pytest.mark.skipif(False)
    def test11_browserWindows(self):
        browserWindows_test(self.driver)
    
    @pytest.mark.skipif(False)
    def test12_alerts(self):
        alerts_test(self.driver)
    
    @pytest.mark.skipif(False)
    def test13_frames(self):
        frames_test(self.driver)

    @pytest.mark.skipif(False)
    def test14_nestedFrames(self):
        nestedFrames_test(self.driver)

    @pytest.mark.skipif(False)
    def test15_modalDialogs(self):
        modalDialogs_test(self.driver)

    @pytest.mark.skipif(False)
    def test16_modalDialogs(self):
        login_test(self.driver, user_data=self.get_json_data())

    @pytest.mark.skipif(False) # ---> Por realizar
    def test17_modalDialogs(self):
        bookStore_test(self.driver)

    @pytest.mark.skipif(False) # ---> Por realizar
    def test18_modalDialogs(self):
        profile_test(self.driver)
    """

    @pytest.mark.skipif(False)
    def test19_modalDialogs(self):
        api_test()

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
    # unittest.main(testRunner=HTMLTestRunner(output=os.getcwd(), report_title="Report by Ismael Sanroman"))
    unittest.main()