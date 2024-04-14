from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://st.rvpdplus.com/direct/en/login" 

    def open(self):
        self.driver.get(self.url)

    def scroll_to_bottom(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()
        time.sleep(2)
    
    def change_login_method(self):
        change_username_button = self.driver.find_element(By.ID, "direct-change-username")
        change_username_button.click()
        time.sleep(2)

    def login(self, email, password):
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "direct-login-submit")

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()
        time.sleep(2)

    def login_with_phone_number(self, username, password):
        self.scroll_to_bottom()
        self.change_login_method()

        phone_number_field = self.driver.find_element(By.ID, "phoneNumber")
        password_field = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "direct-login-submit")

        phone_number_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()
        time.sleep(2)

    def confirm_otp(self, otp):
        self.scroll_to_bottom()

        otp_field = self.driver.find_element(By.ID, "otp")
        otp_field.send_keys(otp)
        next_button = self.driver.find_element(By.XPATH, '//button[text()="Next"]')
        next_button.click()
        time.sleep(2)

    def forgot_password(self):
        self.scroll_to_bottom()
        forgot_path = self.driver.find_element(By.ID, "direct-path-forgot-login")
        forgot_path.click()
        time.sleep(2)