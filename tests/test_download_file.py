import unittest
from tests.conftest import Browser
from pages.selenium_playground_page import *

import requests
import json



# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestDownloadFile(Browser):
    
    def test_download(self):
        page = Selenium_Playground_Page(self.driver)
        download_file = page.download("How to download files using Selenium & Python?")

class TestAPIDownloadFile():

        username = "YOUR_USENAME"
        access_Key = "YOUR_ACCESS_KEY"
    
        #POST_REQUEST
        url = "https://api.lambdatest.com/automation/api/v1/user-files"

        payload={}

        files=[
        ('files',('Lambdainfo.txt',open('/Users/macbookair/Downloads/Lambdainfo.txt','rb'),'text/plain'))
        ]

        headers = {
        'authority': 'api.lambdatest.com',
        'accept': 'application/json',
        }

        response = requests.request("POST", url, auth=(username, access_Key), headers=headers, data=payload, files=files)

        print(response.text)
    

        #PUT_REQUEST
        url = "https://api.lambdatest.com/automation/api/v1/user-files/download"


        payload = json.dumps({
        "key": "Lambdainfo.txt"
        })

        headers = {
        'accept': 'application/octet-stream',
        'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, auth=(username, access_Key), headers=headers, data=payload)
        open('/Users/macbookair/Documents/how_download_files_selenium_python/download/Lambdainfo_API.txt', 'wb').write(response.content)

        print(response.text)
