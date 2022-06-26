from selenium.webdriver.common.keys import Keys
from utils.locators import *
import time


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class Selenium_Playground_Page():

    def __init__(self, driver):
        self.locator = SeleniumPlaygroundPageLocators
        self.driver = driver

    def download(self, text):
        self.driver.find_element(*self.locator.file_download).click()
        self.driver.find_element(*self.locator.data_field).send_keys(text)
        self.driver.find_element(*self.locator.generate_file).click()
        self.driver.find_element(*self.locator.download_button).click()
        time.sleep(5)