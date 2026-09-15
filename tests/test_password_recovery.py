import allure


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Ссылка «Восстановить пароль» открывает страницу восстановления")
    def test_recover_password_link_opens_forgot_password_page(
        self, login_page, forgot_password_page
    ):
        login_page.open()

        login_page.click_recover_password()

        assert forgot_password_page.is_open()

    @allure.title("Почта и кнопка «Восстановить» открывают сброс пароля")
    def test_submit_recovery_email_opens_reset_password_page(
        self, forgot_password_page, reset_password_page, recovery_email
    ):
        forgot_password_page.open()

        forgot_password_page.request_password_reset(recovery_email)

        assert reset_password_page.is_open()

    @allure.title("Кнопка видимости пароля делает поле активным")
    def test_password_visibility_icon_activates_password_field(
        self, forgot_password_page, reset_password_page, recovery_email
    ):
        forgot_password_page.open()
        forgot_password_page.request_password_reset(recovery_email)

        reset_password_page.click_password_visibility_icon()

        assert reset_password_page.is_password_field_active()
