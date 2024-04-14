import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import NoSuchElementException
from login_page import LoginPage
from product_page import ProductPage

class TestProductPage(unittest.TestCase):
    def setUp(self):
        self.driver = self.create_driver()  
        self.driver.maximize_window() 
        
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)

        self.folder_name = "screenshots"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        self.product_folder_path = os.path.join(self.folder_name, "product")
        if not os.path.exists(self.product_folder_path):
            os.makedirs(self.product_folder_path)

    def tearDown(self):
        self.driver.quit() 
        
    @staticmethod
    def create_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        return webdriver.Chrome(options=chrome_options)
    
    def login_with_phone_number(self):
        self.login_page.open()
        self.login_page.login_with_phone_number("0972201973", "Be220216")  

        modal = None
        try:
            modal = self.driver.find_element(By.ID, "direct-warning-login")
        except NoSuchElementException:
            pass
        self.assertIsNone(modal, "Modal direct-warning-login appeared after login")  
        self.login_page.confirm_otp("Passed")

        if self.driver.current_url == "https://st.rvpdplus.com/direct/en":
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename =  self.product_folder_path + "/" + timestamp + "_successful_login" + ".png"
            self.driver.save_screenshot(filename)
            self.assertTrue(True)
        else:
            self.fail("Incorrect redirect after successful login")

    def test_product_page_functionality(self):
        initial_url = None
        self.login_with_phone_number()

        self.product_page.purchase_product()
        initial_url = self.driver.current_url
        
        success = self.product_page.verify_current_url()
        if success:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = self.product_folder_path + "/" + timestamp + "_product_page_success" + ".png"
            self.driver.save_screenshot(filename)
            self.assertTrue(success,"Incorrect URL on Product Page")
        else:
            self.fail("Incorrect URL on Product Page")
        
        self.product_page.choose_product_code("1.30A")
        success = self.driver.current_url != initial_url
        if success:
            self.assertTrue(success, "URL not changed after clicking link")
        else:
            self.fail("URL not changed after clicking link")

        initial_url = self.driver.current_url
        self.product_page.key_chassis_number("1234")
        success = self.driver.current_url != initial_url
        if success:
            self.assertTrue(success, "URL not changed after clicking verify button")
        else:
            self.fail("URL not changed after clicking verify button")

if __name__ == "__main__":
    # python test_product_page.py
    unittest.main()
