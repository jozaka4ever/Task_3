import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPasswordPage(BasePage):
    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self._open(Urls.FORGOT_PASSWORD_PAGE)

    def request_password_reset(self, email):
        with allure.step("Ввести почту и нажать «Восстановить»"):
            self._type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)
            self._click(ForgotPasswordPageLocators.RECOVER_BUTTON)

    def is_open(self):
        return self._is_url_and_element_visible(
            Urls.FORGOT_PASSWORD_PAGE,
            ForgotPasswordPageLocators.TITLE,
        )
