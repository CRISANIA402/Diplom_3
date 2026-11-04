import allure

from locators.locators import Locators
from pages.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException

class FeedPage(BasePage):
    @allure.step("Получаем счётчик «Выполнено за всё время»")
    def get_total_done(self):
        return int(self.get_text(Locators.TOTAL_DONE_COUNTER))

    @allure.step("Получаем счётчик «Выполнено за сегодня»")
    def get_today_done(self):
        return int(self.get_text(Locators.TODAY_DONE_COUNTER))

    @allure.step("Читаем номера заказов из раздела «В работе»")
    def get_numbers_in_work(self):
        """Возвращает номера заказов из раздела «В работе».
        Список обновляется в реальном времени, поэтому чтение
        может обгонять перерисовку DOM — повторяем до результата."""
        for _ in range(3):
            try:
                elements = self.find_all(Locators.IN_WORK_NUMBERS)
                numbers = [int(el.text) for el in elements if el.text.strip().isdigit()]
                if numbers:
                    return numbers
            except StaleElementReferenceException:
                continue
        return []
