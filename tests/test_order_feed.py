import allure

from helpers import create_order, get_ingredients
from pages.feed_page import FeedPage
from urls import FEED_URL


class TestOrderFeed:
    @allure.title("Счётчик «Выполнено за всё время» увеличивается после нового заказа")
    def test_total_done_increases(self, driver, registered_user):
        feed = FeedPage(driver)
        feed.open(FEED_URL)
        before = feed.get_total_done()

        create_order(registered_user["token"], get_ingredients()[:2])

        feed.open(FEED_URL)
        after = feed.get_total_done()
        assert after > before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после нового заказа")
    def test_today_done_increases(self, driver, registered_user):
        feed = FeedPage(driver)
        feed.open(FEED_URL)
        before = feed.get_today_done()

        create_order(registered_user["token"], get_ingredients()[:2])

        feed.open(FEED_URL)
        after = feed.get_today_done()
        assert after > before

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_order_number_appears_in_work(self, driver, registered_user):
        response = create_order(registered_user["token"], get_ingredients()[:2])
        order_number = response.json()["order"]["number"]

        feed = FeedPage(driver)
        feed.open(FEED_URL)
        numbers_in_work = feed.get_numbers_in_work()
        assert order_number in numbers_in_work
