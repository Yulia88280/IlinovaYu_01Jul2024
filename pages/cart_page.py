from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        # Нажимаем на кнопку "Добавить в корзину" для указанного товара
        add_to_cart_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'button.btn-default.js-order[attr_item="{item_name}"]'))
        )
        add_to_cart_button.click()

    def go_to_cart(self):
        # Переходим в корзину
        basket_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > a > div'))
        )
        basket_button.click()

    def is_item_in_cart(self, item_name):
        try:
            # Проверяем, есть ли указанный товар в корзине
            item_in_cart = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, f'//span[@class="name_product_item" and text()="{item_name}"]'))
            )
            return item_in_cart is not None
        except:
            return False

    def remove_item_from_cart(self, item_name):
        # Удаляем указанный товар из корзины
        remove_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.delet_pr_bas'))
        )
        remove_button.click()

    def is_item_not_in_cart(self, item_name):
        try:
            # Проверяем, что указанный товар больше не отображается в корзине
            WebDriverWait(self.driver, 30).until_not(
                EC.visibility_of_element_located((By.XPATH, f'//span[@class="name_product_item" and text()="{item_name}"]'))
            )
            return True
        except:
            return False

    def update_item_quantity(self, item_name, quantity):
        # Обновляем количество указанного товара в корзине
        quantity_input = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, f'//span[@class="name_product_item" and text()="{item_name}"]/../../..//input[@type="text"]'))
        )
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def get_item_quantity(self, item_name):
        # Получаем текущее количество указанного товара в корзине
        quantity_input = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, f'//span[@class="name_product_item" and text()="{item_name}"]/../../..//input[@type="text"]'))
        )
        return int(quantity_input.get_attribute("value"))
