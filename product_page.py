from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://st.rvpdplus.com/direct/en/product"

    def open(self):
        self.driver.get(self.url)

    def scroll_to_bottom(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()
        time.sleep(2)

    def verify_current_url(self):
        return self.driver.current_url == self.url

    def purchase_product(self):
        purchase_button = self.driver.find_element(By.XPATH, '//button[text()="Purchase Product"]')
        purchase_button.click()
        time.sleep(2)

    def choose_product_code(self, code):
        xpath = f"//a[contains(@href, 'code={code}')]"
        link_element = self.driver.find_element(By.XPATH, xpath)
        link_element.click()
        time.sleep(2)

    def key_chassis_number(self, chassis):
        chassis_field = self.driver.find_element(By.ID, "chassisNumber")
        chassis_field.send_keys(chassis)
        self.scroll_to_bottom()
        next_button = self.driver.find_element(By.XPATH, '//button[text()="Verify"]')
        next_button.click()
        time.sleep(2)


