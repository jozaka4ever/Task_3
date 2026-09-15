import allure
import requests

from config import BrowserConfig
from urls import Urls


class StellarBurgersApi:
    """Клиент для создания и удаления тестовых пользователей."""

    def __init__(self):
        self._session = requests.Session()

    def close(self):
        self._session.close()

    def create_user(self, user_data):
        with allure.step("Создать тестового пользователя через API"):
            return self._session.post(
                Urls.REGISTER_USER_API,
                json=user_data,
                timeout=BrowserConfig.REQUEST_TIMEOUT,
            )

    def delete_user(self, access_token):
        with allure.step("Удалить тестового пользователя через API"):
            return self._session.delete(
                Urls.USER_API,
                headers={"Authorization": access_token},
                timeout=BrowserConfig.REQUEST_TIMEOUT,
            )
