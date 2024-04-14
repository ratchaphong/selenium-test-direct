import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from forgot_page import ForgotPage
from login_page import LoginPage
import os


class TestForgotPage(unittest.TestCase):
    def setUp(self):
        self.driver = self.create_driver()  
        self.driver.maximize_window() 
        
        self.login_page = LoginPage(self.driver)
        self.forgot_page = ForgotPage(self.driver)

        self.folder_name = "screenshots"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        self.forgot_folder_path = os.path.join(self.folder_name, "forgot")
        if not os.path.exists(self.forgot_folder_path):
            os.makedirs(self.forgot_folder_path)

    def tearDown(self):
        self.driver.quit() 
        
    @staticmethod
    def create_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        return webdriver.Chrome(options=chrome_options)
    
    def forgot(self):
        self.login_page.open()
        self.login_page.forgot_password()  

        if self.driver.current_url == self.forgot_page.url:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename =  self.forgot_folder_path + "/" + timestamp + "_successful_forgot" + ".png"
            self.driver.save_screenshot(filename)
            self.assertTrue(True)
        else:
            self.fail("Incorrect redirect after click forgot password")

    def test_forgot_page_functionality(self):
        self.forgot()
        self.forgot_page.form("1600100791371", "1999-07-05")
        
if __name__ == "__main__":
    # python test_forgot_page.py
    unittest.main()
