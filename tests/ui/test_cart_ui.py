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

        # Добавляем товар в корзину
        cart_page.add_item_to_cart(item_name)
        # Переходим в корзину
        cart_page.go_to_cart()

        # Проверяем, что товар был добавлен в корзину
        assert cart_page.is_item_in_cart(item_name), "Товар не был добавлен в корзину"

    @allure.feature('Cart UI')
    @allure.story('Remove Item from Cart')
    def test_remove_item_from_cart(self, setup):
        driver = setup
        cart_page = CartPage(driver)
        item_name = "Грузди соленые"

        # Добавляем товар в корзину
        cart_page.add_item_to_cart(item_name)
        # Переходим в корзину
        cart_page.go_to_cart()

        # Удаляем товар из корзины
        cart_page.remove_item_from_cart(item_name)

        # Проверяем, что товар был удален из корзины
        assert cart_page.is_item_not_in_cart(item_name), "Товар не был удален из корзины"

    @allure.feature('Cart UI')
    @allure.story('Update Item Quantity')
    def test_update_item_quantity(self, setup):
        driver = setup
        cart_page = CartPage(driver)
        item_name = "Грузди соленые"
        new_quantity = 2

        # Добавляем товар в корзину
        cart_page.add_item_to_cart(item_name)
        # Переходим в корзину
        cart_page.go_to_cart()

        # Обновляем количество товара в корзине
        cart_page.update_item_quantity(item_name, new_quantity)

        # Получаем текущее количество товара в корзине и проверяем, что оно соответствует новому количеству
        updated_quantity = cart_page.get_item_quantity(item_name)
        assert updated_quantity == new_quantity, "Количество товара не было обновлено"
