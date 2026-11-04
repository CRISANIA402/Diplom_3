import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers import generate_user
from urls import CREATE_USER_API, USER_API


@allure.title("Фикстура: браузер Chrome/Firefox")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Запускает каждый тест дважды: в Chrome и в Firefox."""
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Фикстура: пользователь, созданный через API")
@pytest.fixture
def registered_user():
    """Создаёт пользователя через API и удаляет его после теста."""
    user_data = generate_user()
    response = requests.post(CREATE_USER_API, json=user_data)
    token = response.json()["accessToken"]

    yield {"user_data": user_data, "token": token}

    requests.delete(USER_API, headers={"Authorization": token})
