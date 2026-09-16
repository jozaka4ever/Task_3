import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from urls import Urls


class OrderFeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open(self):
        self._open(Urls.ORDER_FEED_PAGE)

    def wait_until_loaded(self):
        self._wait_for_url_and_element(
            Urls.ORDER_FEED_PAGE,
            OrderFeedPageLocators.ALL_TIME_COUNTER,
        )

    def is_open(self):
        return self._is_url_and_element_visible(
            Urls.ORDER_FEED_PAGE,
            OrderFeedPageLocators.TITLE,
        )

    def open_first_order(self):
        with allure.step("Открыть первый заказ в ленте"):
            number = self._get_text(OrderFeedPageLocators.FIRST_ORDER_NUMBER)
            self._click(OrderFeedPageLocators.FIRST_ORDER_CARD)
            return int(number.removeprefix("#"))

    def is_order_details_open(self, order_number):
        return self._is_element_visible(
            OrderFeedPageLocators.order_modal(order_number)
        ) and self._is_url_starting_with(Urls.ORDER_DETAILS_PREFIX)

    def is_order_visible(self, order_number):
        return self._is_element_visible(OrderFeedPageLocators.order_card(order_number))

    def get_all_time_counter(self):
        return int(self._get_text(OrderFeedPageLocators.ALL_TIME_COUNTER))

    def get_today_counter(self):
        return int(self._get_text(OrderFeedPageLocators.TODAY_COUNTER))

    def has_all_time_counter_increased(self, previous_value):
        return self._is_text_matching(
            OrderFeedPageLocators.ALL_TIME_COUNTER,
            lambda text: text.isdigit() and int(text) > previous_value,
        )

    def has_today_counter_increased(self, previous_value):
        return self._is_text_matching(
            OrderFeedPageLocators.TODAY_COUNTER,
            lambda text: text.isdigit() and int(text) > previous_value,
        )

    def is_order_in_progress(self, order_number):
        return self._is_element_visible(
            OrderFeedPageLocators.in_progress_order(order_number)
        )
