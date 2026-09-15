import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from urls import Urls


class ProfilePage(BasePage):
    @allure.step("Перейти в историю заказов")
    def open_order_history(self):
        self._click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self._click(ProfilePageLocators.LOGOUT_BUTTON)

    def is_profile_open(self):
        return self._is_url_and_element_visible(
            Urls.PROFILE_PAGE,
            ProfilePageLocators.ACTIVE_PROFILE_LINK,
        )

    def is_order_history_open(self):
        return self._is_url_and_element_visible(
            Urls.ORDER_HISTORY_PAGE,
            ProfilePageLocators.ACTIVE_ORDER_HISTORY_LINK,
        )

    def get_latest_order_number(self):
        number = self._get_text(ProfilePageLocators.FIRST_HISTORY_ORDER_NUMBER)
        return int(number.removeprefix("#"))
