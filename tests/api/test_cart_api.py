import pytest
import requests
import allure
from conftest import extract_json_from_data

@allure.feature('Корзина')
@allure.story('Добавление товара в корзину')
def test_add_to_cart(base_url, headers):
    url = f"{base_url}/ajax/basketOrder.php"
    payload = {
        "idCookie": "630792",
        "idProd": "178",
        "type": "add"
    }

    response = requests.post(url, json=payload, headers=headers)
    allure.attach(response.text, name='Response Text', attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    try:
        response_json = extract_json_from_data(response.text)
        allure.attach(str(response_json), name='Response JSON', attachment_type=allure.attachment_type.JSON)
        assert response_json["type"] == "add", "Товар не был добавлен в корзину"
    except ValueError as e:
        pytest.fail(f"Response is not a valid JSON: {e}")

@allure.feature('Корзина')
@allure.story('Изменение количества товара в корзине')
def test_update_item_quantity(base_url, headers):
    url = f"{base_url}/ajax/basketOrder.php"
    payload = {
        "idCookie": "630792",
        "idProd": 178,
        "type": "update",
        "quantity": 2
    }

    response = requests.post(url, json=payload, headers=headers)
    allure.attach(response.text, name='Response Text', attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    try:
        response_json = extract_json_from_data(response.text)
        allure.attach(str(response_json), name='Response JSON', attachment_type=allure.attachment_type.JSON)
        assert response_json["type"] == "update", "Количество товара не было изменено"
        assert response_json["quantity"] == 2, "Количество товара не соответствует ожидаемому"
    except ValueError as e:
        pytest.fail(f"Response is not a valid JSON: {e}")

@allure.feature('Корзина')
@allure.story('Удаление товара из корзины')
def test_remove_from_cart(base_url, headers):
    url = f"{base_url}/ajax/basketOrder.php"
    payload = {
        "idCookie": "630792",
        "idProd": 178,
        "type": "delete"
    }

    response = requests.post(url, json=payload, headers=headers)
    allure.attach(response.text, name='Response Text', attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    try:
        response_json = extract_json_from_data(response.text)
        allure.attach(str(response_json), name='Response JSON', attachment_type=allure.attachment_type.JSON)
        assert response_json["type"] == "delete", "Товар не был удален из корзины"
    except ValueError as e:
        pytest.fail(f"Response is not a valid JSON: {e}")
