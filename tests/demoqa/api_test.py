import pytest
import requests
import allure


BASE_URL = "https://demoqa.com"


@allure.epic("API Tests")
@allure.feature("Authorization")
class TestAuth:

    @allure.story("Login with valid credentials")
    def test_login_successful(self):
        payload = {
            "userName": "TestUser123",
            "password": "TestPassword123!"
        }

        with allure.step("POST /Account/v1/Login with valid credentials"):
            response = requests.post(f"{BASE_URL}/Account/v1/Login", json=payload)

        with allure.step("Проверка кода ответа 200"):
            assert response.status_code == 200
            assert "token" in response.json()

    @allure.story("Login with invalid credentials")
    def test_login_unauthorized(self):
        payload = {
            "userName": "WrongUser",
            "password": "WrongPassword"
        }

        with allure.step("POST /Account/v1/Login with invalid credentials"):
            response = requests.post(f"{BASE_URL}/Account/v1/Login", json=payload)

        with allure.step("Проверка кода ответа 401"):
            assert response.status_code == 401
            assert response.json()["message"] == "User not found!"
