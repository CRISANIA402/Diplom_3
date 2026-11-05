import allure
import pytest

from pages.main_page import MainPage
from urls import BASE_URL, FEED_URL


@pytest.fixture
def main_page(driver):
    """Предусловие: созданная и открытая главная страница."""
    page = MainPage(driver)
    page.open(BASE_URL)
    return page


class TestMainFunctionality:
    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, main_page):
        main_page.click_order_feed()
        main_page.wait_for_url(FEED_URL)
        assert main_page.get_current_url() == FEED_URL
        main_page.click_constructor()
        main_page.wait_for_url(BASE_URL)
        assert main_page.get_current_url() == BASE_URL


    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed(self, main_page):
        main_page.click_order_feed()
        main_page.wait_for_url(FEED_URL)
        assert main_page.get_current_url() == FEED_URL

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_modal_opens(self, main_page):
        main_page.open_ingredient_details()
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Окно с деталями закрывается крестиком")
    def test_ingredient_modal_closes(self, main_page):
        main_page.open_ingredient_details()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title("Проверка увеличения числа на счётчике при добавлении ингредиента в заказ")
    def test_ingredient_counter_increases(self, main_page):
        main_page.add_ingredient_to_burger()
        assert main_page.get_ingredient_counter_value() == 2
