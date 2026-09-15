from selenium.webdriver.common.by import By

from texts import HeaderTexts


class BasePageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        f"//header//a[normalize-space(.)='{HeaderTexts.CONSTRUCTOR}']",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        f"//header//a[normalize-space(.)='{HeaderTexts.ORDER_FEED}']",
    )
    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        f"//header//a[normalize-space(.)='{HeaderTexts.PERSONAL_ACCOUNT}']",
    )
