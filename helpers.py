import random
import string

import requests

from urls import (CREATE_USER_API, LOGIN_USER_API, ORDERS_API,
                  INGREDIENTS_API)


def generate_user():
    """Создаёт случайные данные пользователя."""
    name = "Тест_" + "".join(random.choices(string.ascii_lowercase, k=6))
    email = "ui_" + "".join(random.choices(string.ascii_lowercase, k=6)) + "@yandex.ru"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    return {"name": name, "email": email, "password": password}


def register_user(user_data):
    """Регистрирует пользователя через API, возвращает ответ."""
    return requests.post(CREATE_USER_API, json=user_data)


def login_user(user_data):
    """Логинит пользователя через API, возвращает ответ с accessToken."""
    return requests.post(LOGIN_USER_API, json={
        "email": user_data["email"],
        "password": user_data["password"],
    })


def get_ingredients():
    """Возвращает список хешей доступных ингредиентов."""
    response = requests.get(INGREDIENTS_API)
    ingredients = response.json()["data"]
    return [ingredient["_id"] for ingredient in ingredients]


def create_order(token, ingredient_hashes):
    """Создаёт заказ через API от имени пользователя. Возвращает ответ."""
    headers = {"Authorization": token}
    payload = {"ingredients": ingredient_hashes}
    return requests.post(ORDERS_API, headers=headers, json=payload)
