import allure

from config import BrowserConfig
from data import IngredientTestData
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from texts import MainPageTexts
from urls import Urls


class MainPage(BasePage):
    @allure.step("Открыть конструктор")
    def open(self):
        self._open(Urls.MAIN_PAGE)

    def wait_until_loaded(self):
        self._wait_for_url_and_element(Urls.MAIN_PAGE, MainPageLocators.TITLE)

    def is_open(self):
        return self._is_url_and_element_visible(Urls.MAIN_PAGE, MainPageLocators.TITLE)

    def open_ingredient_details(self, ingredient_name):
        with allure.step("Открыть детали ингредиента"):
            self._click(MainPageLocators.ingredient_card(ingredient_name))

    @allure.step("Закрыть детали ингредиента")
    def close_ingredient_details(self):
        self._click(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    def is_ingredient_details_open(self, ingredient_name):
        modal_is_visible = self._is_element_visible(MainPageLocators.INGREDIENT_MODAL)
        name_is_visible = self._is_element_visible(
            MainPageLocators.ingredient_name_in_modal(ingredient_name)
        )
        return (
            modal_is_visible
            and name_is_visible
            and self._driver.current_url.startswith(Urls.INGREDIENT_DETAILS_PREFIX)
        )

    def is_ingredient_details_closed(self):
        return self._is_element_invisible(MainPageLocators.INGREDIENT_MODAL)

    def get_ingredient_counter(self, ingredient_name):
        return int(self._get_text(MainPageLocators.ingredient_counter(ingredient_name)))

    def add_ingredient_to_order(self, ingredient_name):
        with allure.step("Добавить ингредиент в заказ"):
            self._drag_and_drop(
                MainPageLocators.ingredient_card(ingredient_name),
                MainPageLocators.BASKET,
            )

    def is_ingredient_counter_equal(self, ingredient_name, expected_value):
        locator = MainPageLocators.ingredient_counter(ingredient_name)
        return self._is_condition_met(
            lambda driver: driver.find_element(*locator).text == str(expected_value)
        )

    @allure.step("Собрать стандартный заказ")
    def build_standard_order(self):
        self._drag_and_drop(
            MainPageLocators.ingredient_card(IngredientTestData.BUN_NAME),
            MainPageLocators.BASKET,
        )
        self._drag_and_drop(
            MainPageLocators.ingredient_card(IngredientTestData.SAUCE_NAME),
            MainPageLocators.BASKET,
        )

    @allure.step("Нажать «Оформить заказ»")
    def submit_order(self):
        self._click(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_order_created(self):
        def actual_order_number_is_visible(driver):
            elements = driver.find_elements(*MainPageLocators.ORDER_NUMBER)
            return bool(
                elements
                and elements[0].text.isdigit()
                and elements[0].text != MainPageTexts.ORDER_NUMBER_PLACEHOLDER
            )

        return self._is_condition_met(
            actual_order_number_is_visible,
            BrowserConfig.ORDER_WAIT_TIMEOUT,
        )

    def get_created_order_number(self):
        def get_actual_order_number(driver):
            elements = driver.find_elements(*MainPageLocators.ORDER_NUMBER)
            if (
                elements
                and elements[0].text.isdigit()
                and elements[0].text != MainPageTexts.ORDER_NUMBER_PLACEHOLDER
            ):
                return elements[0]
            return False

        number_element = self._wait.until(get_actual_order_number)
        return int(number_element.text)

    @allure.step("Закрыть окно созданного заказа")
    def close_order_modal(self):
        self._click(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
