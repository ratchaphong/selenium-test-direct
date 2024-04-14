import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import NoSuchElementException
from login_page import LoginPage

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = self.create_driver()  # สร้าง WebDriver โดยใช้ค่าที่ระบุจาก command line
        self.login_page = LoginPage(self.driver)

        # ตรวจสอบว่าโฟลเดอร์ screenshots มีอยู่หรือไม่
        self.folder_name = "screenshots"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        # ตรวจสอบว่าโฟลเดอร์ login มีอยู่ภายในโฟลเดอร์ screenshots หรือไม่
        self.login_folder_path = os.path.join(self.folder_name, "login")
        if not os.path.exists(self.login_folder_path):
            os.makedirs(self.login_folder_path)

    def tearDown(self):
        self.driver.quit() 
        
    @staticmethod
    def create_driver():
        return webdriver.Chrome()

    def test_successful_login(self):
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
            filename =  self.login_folder_path + "/" + timestamp + "_successful_login" + ".png"
            self.driver.save_screenshot(filename)
            self.assertTrue(True)
        else:
            self.fail("Incorrect redirect after successful login")

    def test_invalid_login(self):
        self.login_page.open()
        self.login_page.login("ratchaphongc1@gmail.com", "TQD1234") 
        modal = None
        try:
            modal = self.driver.find_element(By.ID, "direct-warning-login")
        except:
            pass

        if modal:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename =  self.login_folder_path + "/" + timestamp + "_unsuccessful_login" + ".png"
            self.driver.save_screenshot(filename)
            self.assertTrue(modal.is_displayed())
        else:
            self.fail("Unsuccessful login modal not displayed")

if __name__ == "__main__":
    # python test_login_page.py
    partial = True
    if (partial):
        # ระบุฟังก์ชันที่ต้องการทดสอบ
        test_functions = ["test_successful_login"]

        # สร้าง TestSuite เพื่อรันเฉพาะฟังก์ชันที่ระบุ
        suite = unittest.TestSuite()
        for test_func in test_functions:
            suite.addTest(TestLoginPage(test_func))

        # รัน TestSuite
        unittest.TextTestRunner().run(suite)
    else: 
        unittest.main()

      

