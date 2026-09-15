from selenium.webdriver.common.by import By

from texts import OrderFeedPageTexts


class OrderFeedPageLocators:
    TITLE = (
        By.XPATH,
        f"//h1[normalize-space()='{OrderFeedPageTexts.TITLE}']",
    )
    FIRST_ORDER_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'OrderHistory_link__')])[1]",
    )
    FIRST_ORDER_NUMBER = (
        By.XPATH,
        (
            "(//a[contains(@class, 'OrderHistory_link__')]"
            "//p[starts-with(normalize-space(), '#')])[1]"
        ),
    )
    ALL_TIME_COUNTER = (
        By.XPATH,
        (
            f"//p[normalize-space()='{OrderFeedPageTexts.ALL_TIME_COUNTER}']"
            "/following-sibling::p"
        ),
    )
    TODAY_COUNTER = (
        By.XPATH,
        (
            f"//p[normalize-space()='{OrderFeedPageTexts.TODAY_COUNTER}']"
            "/following-sibling::p"
        ),
    )

    @staticmethod
    def order_card(order_number):
        formatted_number = f"#{order_number:06d}"
        return (
            By.XPATH,
            (
                "//a[contains(@class, 'OrderHistory_link__')]"
                f"[.//p[normalize-space()='{formatted_number}']]"
            ),
        )

    @staticmethod
    def order_modal(order_number):
        formatted_number = f"#{order_number:06d}"
        return (
            By.XPATH,
            (
                "//section[contains(@class, 'Modal_modal_opened__')]"
                f"[.//p[normalize-space()='{formatted_number}']]"
            ),
        )

    @staticmethod
    def in_progress_order(order_number):
        formatted_number = f"{order_number:06d}"
        return (
            By.XPATH,
            (
                f"//p[normalize-space()='{OrderFeedPageTexts.IN_PROGRESS}']"
                "/following-sibling::ul"
                f"//li[normalize-space()='{formatted_number}']"
            ),
        )
