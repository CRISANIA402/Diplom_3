import allure

from locators.locators import Locators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Кликаем по кнопке «Конструктор»")
    def click_constructor(self):
        self.click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликаем по кнопке «Лента заказов»")
    def click_order_feed(self):
        self.click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем по булке «Флюоресцентная булка R2-D3»")
    def open_ingredient_details(self):
        self.click(Locators.INGREDIENT)

    @allure.step("Проверяем, что модальное окно ингредиента отображается")
    def is_ingredient_modal_visible(self):
        return self.find(Locators.INGREDIENT_MODAL_HEADER).is_displayed()

    @allure.step("Закрываем модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(Locators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверяем, что модальное окно ингредиента закрылось")
    def is_ingredient_modal_closed(self):
        return self.wait_for_invisible(Locators.INGREDIENT_MODAL_HEADER)

    @allure.step("Перетаскиваем булку в конструктор")
    def add_ingredient_to_burger(self):
        """Булка кладётся в оба слоя, поэтому счётчик становится 2."""
        card = self.find(Locators.INGREDIENT_CARD)
        target = self.find(Locators.CONSTRUCTOR_AREA)
        self.drag_and_drop(card, target)

    @allure.step("Получаем значение счётчика булки")
    def get_ingredient_counter_value(self):
        return int(self.find_present(Locators.INGREDIENT_COUNTER).text)
