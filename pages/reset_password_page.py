import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ResetPasswordPage(BasePage):
    @allure.step("Нажать на кнопку показать или скрыть пароль")
    def click_password_visibility_icon(self):
        self._click(ResetPasswordPageLocators.PASSWORD_VISIBILITY_ICON)

    def is_open(self):
        return self._is_url_and_element_visible(
            Urls.RESET_PASSWORD_PAGE,
            ResetPasswordPageLocators.TITLE,
        )

    def is_password_field_active(self):
        return self._is_element_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT)
