import pytest
from selenium import webdriver
import re
import json

@pytest.fixture(scope="session")
def base_url():
    return "https://www.sibdar-spb.ru"

@pytest.fixture(scope="session")
def session_id():
    return "ggIeAMkqKGmqJjPI2lMxArpRo14e0Gy1"

@pytest.fixture
def headers(session_id):
    return {
        "Cookie": f"PHPSESSID={session_id}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.sibdar-spb.ru")
    yield driver
    driver.quit()

# Определяем функцию extract_json_from_data
def extract_json_from_data(response_text):
    try:
        if response_text:
            match = re.search(r'data: ({.*})', response_text)
            if match:
                json_data = match.group(1)
                return json.loads(json_data)
            else:
                raise ValueError("JSON data not found in the response")
        else:
            raise ValueError("Response text is empty")
    except Exception as e:
        raise ValueError(f"Failed to parse JSON from response: {e}")
