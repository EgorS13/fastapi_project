import requests
import pytest
from openapi_spec_validator import openapi_v3_spec_validator
import json

# Указываем URL для OpenAPI спецификации и API
BASE_URL = "http://127.0.0.1:8000"
SPEC_URL = f"{BASE_URL}/openapi.json"

# Проверка корректности OpenAPI спецификации
def test_openapi_spec():
    response = requests.get(SPEC_URL)
    assert response.status_code == 200
    spec = response.json()
    # Валидируем спецификацию OpenAPI с помощью openapi_spec_validator
    openapi_v3_spec_validator.validate(spec)

# Тестирование эндпоинта получения всех элементов
def test_get_items():
    response = requests.get(f"{BASE_URL}/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Проверяем, что ответ — это список

# Тестирование эндпоинта создания элемента
def test_create_item():
    item_data = {"name": "Item 1", "description": "This is item 1"}
    response = requests.post(f"{BASE_URL}/items", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == item_data["name"]
    assert response.json()["description"] == item_data["description"]

# Тестирование эндпоинта получения элемента по ID
def test_get_item():
    response = requests.get(f"{BASE_URL}/items/0")
    assert response.status_code == 200
    assert "name" in response.json()

# Тестирование эндпоинта обновления элемента
def test_update_item():
    updated_data = {"name": "Updated Item", "description": "Updated description"}
    response = requests.put(f"{BASE_URL}/items/0", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["description"] == updated_data["description"]

# Тестирование эндпоинта удаления элемента
def test_delete_item():
    response = requests.delete(f"{BASE_URL}/items/0")
    assert response.status_code == 200
    assert "name" in response.json()