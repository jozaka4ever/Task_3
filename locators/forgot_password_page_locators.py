from selenium.webdriver.common.by import By

from texts import ForgotPasswordPageTexts


class ForgotPasswordPageLocators:
    TITLE = (
        By.XPATH,
        f"//h2[normalize-space()='{ForgotPasswordPageTexts.TITLE}']",
    )
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    RECOVER_BUTTON = (
        By.XPATH,
        f"//button[normalize-space()='{ForgotPasswordPageTexts.RECOVER_BUTTON}']",
    )
