import allure

from data import IngredientTestData


@allure.feature("Основная функциональность")
class TestMainFunctionality:
    @allure.title("Ссылка «Конструктор» открывает конструктор")
    def test_constructor_link_opens_main_page(self, order_feed_page, main_page):
        order_feed_page.open()

        order_feed_page.click_constructor()

        assert main_page.is_open()

    @allure.title("Ссылка «Лента заказов» открывает ленту")
    def test_order_feed_link_opens_order_feed(self, main_page, order_feed_page):
        main_page.open()

        main_page.click_order_feed()

        assert order_feed_page.is_open()

    @allure.title("Клик по ингредиенту открывает его детали")
    def test_ingredient_click_opens_details_modal(self, main_page):
        main_page.open()

        main_page.open_ingredient_details(IngredientTestData.BUN_NAME)

        assert main_page.is_ingredient_details_open(IngredientTestData.BUN_NAME)

    @allure.title("Крестик закрывает детали ингредиента")
    def test_close_icon_closes_ingredient_details(self, main_page):
        main_page.open()
        main_page.open_ingredient_details(IngredientTestData.BUN_NAME)

        main_page.close_ingredient_details()

        assert main_page.is_ingredient_details_closed()

    @allure.title("Добавление ингредиента увеличивает его счётчик")
    def test_add_ingredient_increases_counter(self, main_page):
        main_page.open()
        counter_before = main_page.get_ingredient_counter(IngredientTestData.SAUCE_NAME)

        main_page.add_ingredient_to_order(IngredientTestData.SAUCE_NAME)

        assert main_page.is_ingredient_counter_equal(
            IngredientTestData.SAUCE_NAME,
            counter_before + 1,
        )

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, authorized_main_page):
        authorized_main_page.build_standard_order()

        authorized_main_page.submit_order()

        assert authorized_main_page.is_order_created()
