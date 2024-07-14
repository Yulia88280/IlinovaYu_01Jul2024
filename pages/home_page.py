from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.CSS_SELECTOR, 'button.btn-default.js-order[attr_item="Грузди соленые"]')
        self.cart_count = (By.CSS_SELECTOR, 'span.count_bask_right')
        self.basket_button = (By.CSS_SELECTOR, 'a.bask_btn_right')

    def add_item_to_cart(self):
        self.click_element(*self.add_to_cart_button)

    def open_cart(self):
        self.click_element(*self.basket_button)

    def get_cart_count(self):
        return self.find_element(*self.cart_count).text
