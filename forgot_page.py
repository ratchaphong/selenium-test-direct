from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ForgotPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://st.rvpdplus.com/direct/en/forgot" 

    def open(self):
        self.driver.get(self.url)

    def form(self, card_number, date_of_birth):
        card_number_field = self.driver.find_element(By.ID, "citizenNo")
        date_of_birth_field = self.driver.find_element(By.ID, "dateOfBirth")
        next_button = self.driver.find_element(By.XPATH, '//button[text()="Next"]')
        card_number_field.send_keys(card_number)
        date_of_birth_field.clear() 
        date_of_birth_field.send_keys(date_of_birth)
      
        next_button.click()
        time.sleep(2)
    