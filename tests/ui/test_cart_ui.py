import pytest
import allure
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestCartUI:

    @allure.feature('Cart UI')
    @allure.story('Add Item to Cart')
    def test_add_item_to_cart(self, setup):
        driver = setup
        cart_page = CartPage(driver)
        item_name = "Грузди соленые"

        try:
            # Добавляем товар в корзину
            cart_page.add_item_to_cart(item_name)
            # Переходим в корзину
            cart_page.go_to_cart()

            # Проверяем, что товар был добавлен в корзину
            assert cart_page.is_item_in_cart(item_name), "Товар не был добавлен в корзину"
        except Exception as e:
            # При возникновении ошибки прикрепляем скриншот и исходный код страницы
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise e

    @allure.feature('Cart UI')
    @allure.story('Remove Item from Cart')
    def test_remove_item_from_cart(self, setup):
        driver = setup
        cart_page = CartPage(driver)
        item_name = "Грузди соленые"

        try:
            # Добавляем товар в корзину
            cart_page.add_item_to_cart(item_name)
            # Переходим в корзину
            cart_page.go_to_cart()

            # Удаляем товар из корзины
            cart_page.remove_item_from_cart(item_name)

            # Проверяем, что товар был удален из корзины
            assert cart_page.is_item_not_in_cart(item_name), "Товар не был удален из корзины"
        except Exception as e:
            # При возникновении ошибки прикрепляем скриншот и исходный код страницы
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise e

    @allure.feature('Cart UI')
    @allure.story('Update Item Quantity')
    def test_update_item_quantity(self, setup):
        driver = setup
        cart_page = CartPage(driver)
        item_name = "Грузди соленые"
        new_quantity = 2

        try:
            # Добавляем товар в корзину
            cart_page.add_item_to_cart(item_name)
            # Переходим в корзину
            cart_page.go_to_cart()

            # Обновляем количество товара в корзине
            cart_page.update_item_quantity(item_name, new_quantity)

            # Получаем текущее количество товара в корзине и проверяем, что оно соответствует новому количеству
            updated_quantity = cart_page.get_item_quantity(item_name)
            assert updated_quantity == new_quantity, "Количество товара не было обновлено"
        except Exception as e:
            # При возникновении ошибки прикрепляем скриншот и исходный код страницы
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise e
