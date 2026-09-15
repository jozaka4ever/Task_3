import allure


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Ссылка «Личный кабинет» открывает профиль")
    def test_personal_account_link_opens_profile(
        self, authorized_main_page, profile_page
    ):
        authorized_main_page.click_personal_account()

        assert profile_page.is_profile_open()

    @allure.title("Ссылка «История заказов» открывает историю")
    def test_order_history_link_opens_order_history(
        self, authorized_main_page, profile_page
    ):
        authorized_main_page.click_personal_account()
        profile_page.open_order_history()

        assert profile_page.is_order_history_open()

    @allure.title("Кнопка «Выход» завершает сессию")
    def test_logout_button_opens_login_page(
        self, authorized_main_page, profile_page, login_page
    ):
        authorized_main_page.click_personal_account()

        profile_page.logout()

        assert login_page.is_open()
