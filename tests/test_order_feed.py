import allure


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик по заказу открывает его детали")
    def test_order_click_opens_order_details(self, order_feed_page):
        order_feed_page.open()

        order_number = order_feed_page.open_first_order()

        assert order_feed_page.is_order_details_open(order_number)

    @allure.title("Заказ из истории пользователя отображается в общей ленте")
    def test_history_order_is_visible_in_order_feed(
        self, placed_order, authorized_main_page, profile_page, order_feed_page
    ):
        authorized_main_page.click_personal_account()
        profile_page.open_order_history()
        history_order_number = profile_page.get_latest_order_number()

        profile_page.click_order_feed()

        assert order_feed_page.is_order_visible(history_order_number)

    @allure.title("Новый заказ увеличивает счётчик за всё время")
    def test_new_order_increases_all_time_counter(self, placed_order, order_feed_page):
        _, all_time_before, _ = placed_order
        order_feed_page.open()

        assert order_feed_page.has_all_time_counter_increased(all_time_before)

    @allure.title("Новый заказ увеличивает счётчик за сегодня")
    def test_new_order_increases_today_counter(self, placed_order, order_feed_page):
        _, _, today_before = placed_order
        order_feed_page.open()

        assert order_feed_page.has_today_counter_increased(today_before)

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_new_order_number_appears_in_progress(self, placed_order, order_feed_page):
        order_number, _, _ = placed_order
        order_feed_page.open()

        assert order_feed_page.is_order_in_progress(order_number)
