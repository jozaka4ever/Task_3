from http import HTTPStatus

import allure
import pytest
from selenium import webdriver

from api.stellar_burgers_api import StellarBurgersApi
from config import BrowserConfig
from data import UserTestData
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


def _create_driver(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument(
            f"--window-size={BrowserConfig.WINDOW_WIDTH},{BrowserConfig.WINDOW_HEIGHT}"
        )
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=options)

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(BrowserConfig.WINDOW_WIDTH, BrowserConfig.WINDOW_HEIGHT)
    return driver


@pytest.fixture(params=BrowserConfig.BROWSERS, ids=BrowserConfig.BROWSERS)
def driver(request):
    browser = _create_driver(request.param)
    yield browser

    reports = (
        getattr(request.node, "rep_setup", None),
        getattr(request.node, "rep_call", None),
    )
    if any(report and report.failed for report in reports):
        allure.attach(
            browser.get_screenshot_as_png(),
            name=f"failure-{request.param}",
            attachment_type=allure.attachment_type.PNG,
        )
    browser.quit()


@pytest.fixture
def api_client():
    client = StellarBurgersApi()
    yield client
    client.close()


@pytest.fixture
def registered_user(api_client):
    user_data = UserTestData.generate_user()
    create_response = api_client.create_user(user_data)
    if create_response.status_code != HTTPStatus.OK:
        pytest.fail(
            "Не удалось создать пользователя для предусловия: "
            f"HTTP {create_response.status_code}"
        )

    access_token = create_response.json().get("accessToken")
    if not access_token:
        pytest.fail("API не вернул accessToken для тестового пользователя")

    yield user_data

    delete_response = api_client.delete_user(access_token)
    if delete_response.status_code != HTTPStatus.ACCEPTED:
        pytest.fail(
            "Не удалось удалить тестового пользователя: "
            f"HTTP {delete_response.status_code}"
        )


@pytest.fixture
def recovery_email():
    return UserTestData.generate_email()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def reset_password_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def authorized_main_page(login_page, main_page, registered_user):
    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])
    main_page.wait_until_loaded()
    return main_page


@pytest.fixture
def placed_order(authorized_main_page, order_feed_page):
    order_feed_page.open()
    order_feed_page.wait_until_loaded()
    all_time_before = order_feed_page.get_all_time_counter()
    today_before = order_feed_page.get_today_counter()

    order_feed_page.click_constructor()
    authorized_main_page.wait_until_loaded()
    authorized_main_page.build_standard_order()
    authorized_main_page.submit_order()
    order_number = authorized_main_page.get_created_order_number()
    authorized_main_page.close_order_modal()

    return order_number, all_time_before, today_before
