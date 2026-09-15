from selenium.webdriver.common.by import By

from texts import ProfilePageTexts


class ProfilePageLocators:
    ACTIVE_PROFILE_LINK = (
        By.XPATH,
        (
            f"//a[normalize-space()='{ProfilePageTexts.PROFILE_LINK}' "
            "and contains(@class, 'Account_link_active__')]"
        ),
    )
    ORDER_HISTORY_LINK = (
        By.XPATH,
        f"//a[normalize-space()='{ProfilePageTexts.ORDER_HISTORY_LINK}']",
    )
    ACTIVE_ORDER_HISTORY_LINK = (
        By.XPATH,
        (
            f"//a[normalize-space()='{ProfilePageTexts.ORDER_HISTORY_LINK}' "
            "and contains(@class, 'Account_link_active__')]"
        ),
    )
    LOGOUT_BUTTON = (
        By.XPATH,
        f"//button[normalize-space()='{ProfilePageTexts.LOGOUT_BUTTON}']",
    )
    FIRST_HISTORY_ORDER_NUMBER = (
        By.XPATH,
        (
            "(//a[contains(@class, 'OrderHistory_link__')]"
            "//p[starts-with(normalize-space(), '#')])[1]"
        ),
    )
