import unittest
from tests.conftest import Browser
from pages.selenium_playground_page import *



# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestDownloadFile(Browser):

    def test_download(self):
        page = Selenium_Playground_Page(self.driver)
        download_file = page.download("lorem ipsum")
