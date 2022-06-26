import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser(unittest.TestCase):

    def setUp(self):
        PATH = "/Users/macbookair/Desktop/how_download_files_selenium_python/download"
        options = Options()
        prefs = {"download.default_directory" : PATH};
        options.add_experimental_option("prefs",prefs);
        self.driver = webdriver.Chrome(options=options)

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", PATH)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        #self.driver = webdriver.Firefox(firefox_profile=profile)

        #safari
        #self.driver = webdriver.Safari()



        self.driver.get("https://www.lambdatest.com/selenium-playground/")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
