from selenium.webdriver.common.by import By

from texts import MainPageTexts


class MainPageLocators:
    TITLE = (By.XPATH, f"//h1[normalize-space()='{MainPageTexts.TITLE}']")
    BASKET = (
        By.CSS_SELECTOR,
        "section[class*='BurgerConstructor_basket__']",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        f"//button[normalize-space()='{MainPageTexts.PLACE_ORDER_BUTTON}']",
    )
    INGREDIENT_MODAL = (
        By.XPATH,
        (
            "//section[contains(@class, 'Modal_modal_opened__')]"
            f"[.//h2[normalize-space()='{MainPageTexts.INGREDIENT_DETAILS_TITLE}']]"
        ),
    )
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        (
            "//section[contains(@class, 'Modal_modal_opened__')]"
            f"[.//h2[normalize-space()='{MainPageTexts.INGREDIENT_DETAILS_TITLE}']]"
            "//button[contains(@class, 'Modal_modal__close_modified__')]"
        ),
    )
    ORDER_NUMBER = (
        By.XPATH,
        (
            "//section[contains(@class, 'Modal_modal_opened__')]"
            f"[.//p[normalize-space()='{MainPageTexts.ORDER_IDENTIFIER}']]"
            "//h2[contains(@class, 'text_type_digits-large')]"
        ),
    )
    ORDER_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        (
            "//section[contains(@class, 'Modal_modal_opened__')]"
            f"[.//p[normalize-space()='{MainPageTexts.ORDER_IDENTIFIER}']]"
            "//button[contains(@class, 'Modal_modal__close_modified__')]"
        ),
    )

    @staticmethod
    def ingredient_card(ingredient_name):
        return (
            By.XPATH,
            (
                "//a[contains(@href, '/ingredient/')]"
                f"[.//p[normalize-space()='{ingredient_name}']]"
            ),
        )

    @staticmethod
    def ingredient_counter(ingredient_name):
        return (
            By.XPATH,
            (
                "//a[contains(@href, '/ingredient/')]"
                f"[.//p[normalize-space()='{ingredient_name}']]"
                "//div[contains(@class, 'counter')]//p"
            ),
        )

    @staticmethod
    def ingredient_name_in_modal(ingredient_name):
        return (
            By.XPATH,
            (
                "//section[contains(@class, 'Modal_modal_opened__')]"
                f"[.//h2[normalize-space()='{MainPageTexts.INGREDIENT_DETAILS_TITLE}']]"
                f"//p[normalize-space()='{ingredient_name}']"
            ),
        )
