import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        self._open(Urls.LOGIN_PAGE)

    @allure.step("Перейти к восстановлению пароля")
    def click_recover_password(self):
        self._click(LoginPageLocators.RECOVER_PASSWORD_LINK)

    def login(self, email, password):
        with allure.step("Войти под тестовым пользователем"):
            self._type_text(LoginPageLocators.EMAIL_INPUT, email)
            self._type_text(LoginPageLocators.PASSWORD_INPUT, password)
            self._click(LoginPageLocators.LOGIN_BUTTON)

    def is_open(self):
        return self._is_url_and_element_visible(
            Urls.LOGIN_PAGE, LoginPageLocators.TITLE
        )
