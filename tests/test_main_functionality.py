import allure

from pages.main_page import MainPage
from urls import BASE_URL, FEED_URL


@allure.title("Переход по клику на «Конструктор»")
def test_navigate_to_constructor(driver):
    page = MainPage(driver)
    page.open(FEED_URL)
    page.click_constructor()
    page.wait_for_url(BASE_URL)


@allure.title("Переход по клику на «Лента заказов»")
def test_navigate_to_order_feed(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.click_order_feed()
    page.wait_for_url(FEED_URL)


@allure.title("Клик по ингредиенту открывает окно с деталями")
def test_ingredient_modal_opens(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.open_ingredient_details()
    assert page.is_ingredient_modal_visible()


@allure.title("Окно с деталями закрывается крестиком")
def test_ingredient_modal_closes(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.open_ingredient_details()
    page.close_ingredient_modal()
    assert page.is_ingredient_modal_closed()


@allure.title("Проверка увеличения числа на счётчике при добавлении ингредиента в заказ")
def test_ingredient_counter_increases(driver):
    driver.get(BASE_URL)
    main_page = MainPage(driver)
    main_page.add_ingredient_to_burger()
    assert main_page.get_ingredient_counter_value() == 2
    