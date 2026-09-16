import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from config import BrowserConfig
from locators.base_page_locators import BasePageLocators


class BasePage:
    """Общие ожидания и действия для всех Page Object."""

    DRAG_EVENTS = ("dragstart", "dragenter", "dragover", "drop", "dragend")

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, BrowserConfig.WAIT_TIMEOUT)

    def _open(self, url):
        self._driver.get(url)

    def _find_visible(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def _find_clickable(self, locator):
        return self._wait.until(ec.element_to_be_clickable(locator))

    def _click(self, locator):
        element = self._find_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self._wait.until(
                lambda driver: self._click_when_unobstructed(driver, locator)
            )

    @staticmethod
    def _click_when_unobstructed(driver, locator):
        try:
            driver.find_element(*locator).click()
            return True
        except (ElementClickInterceptedException, StaleElementReferenceException):
            return False

    def _type_text(self, locator, text):
        element = self._find_visible(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find_visible(locator).text

    def _wait_for_text(self, locator, predicate, timeout=None):
        """Дождаться видимого элемента с текстом, удовлетворяющим условию."""

        def matching_text(driver):
            try:
                element = ec.visibility_of_element_located(locator)(driver)
                if element:
                    text = element.text
                    return text if predicate(text) else False
                return False
            except StaleElementReferenceException:
                return False

        wait = self._wait if timeout is None else WebDriverWait(self._driver, timeout)
        return wait.until(matching_text)

    def _is_text_matching(self, locator, predicate, timeout=None):
        try:
            self._wait_for_text(locator, predicate, timeout)
            return True
        except TimeoutException:
            return False

    def _is_url_starting_with(self, prefix):
        return self._is_condition_met(
            lambda driver: driver.current_url.startswith(prefix)
        )

    def _is_url_and_element_visible(self, url, locator):
        try:
            self._wait.until(ec.url_to_be(url))
            self._wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _wait_for_url_and_element(self, url, locator):
        self._wait.until(ec.url_to_be(url))
        self._wait.until(ec.visibility_of_element_located(locator))

    def _is_element_visible(self, locator, timeout=None):
        wait = self._wait if timeout is None else WebDriverWait(self._driver, timeout)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _is_element_invisible(self, locator):
        try:
            return bool(self._wait.until(ec.invisibility_of_element_located(locator)))
        except TimeoutException:
            return False

    def _is_condition_met(self, condition, timeout=None):
        wait = self._wait if timeout is None else WebDriverWait(self._driver, timeout)
        try:
            return bool(wait.until(condition))
        except TimeoutException:
            return False

    def _drag_and_drop(self, source_locator, target_locator):
        source = self._find_visible(source_locator)
        target = self._find_visible(target_locator)
        script = (
            "const source=arguments[0],target=arguments[1],names=arguments[2];"
            "const transfer=new DataTransfer();"
            "for(const name of names){"
            "const receiver=(name===names[0]||name===names[4])?source:target;"
            "receiver.dispatchEvent(new DragEvent(name,"
            "{bubbles:true,cancelable:true,dataTransfer:transfer}));}"
        )
        self._driver.execute_script(script, source, target, list(self.DRAG_EVENTS))

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self._click(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def click_order_feed(self):
        self._click(BasePageLocators.ORDER_FEED_LINK)

    @allure.step("Перейти в личный кабинет")
    def click_personal_account(self):
        self._click(BasePageLocators.PERSONAL_ACCOUNT_LINK)
