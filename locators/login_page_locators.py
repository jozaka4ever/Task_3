from selenium.webdriver.common.by import By

from texts import LoginPageTexts


class LoginPageLocators:
    TITLE = (By.XPATH, f"//h2[normalize-space()='{LoginPageTexts.TITLE}']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (
        By.XPATH,
        f"//button[normalize-space()='{LoginPageTexts.LOGIN_BUTTON}']",
    )
    RECOVER_PASSWORD_LINK = (
        By.XPATH,
        f"//a[normalize-space()='{LoginPageTexts.RECOVER_PASSWORD_LINK}']",
    )
