from selenium.webdriver.common.by import By

from texts import ResetPasswordPageTexts


class ResetPasswordPageLocators:
    TITLE = (
        By.XPATH,
        f"//h2[normalize-space()='{ResetPasswordPageTexts.TITLE}']",
    )
    PASSWORD_VISIBILITY_ICON = (
        By.XPATH,
        (
            f"//input[@name='{ResetPasswordPageTexts.PASSWORD_INPUT_NAME}']"
            "/following-sibling::div[contains(@class, 'input__icon-action')]"
        ),
    )
    ACTIVE_PASSWORD_INPUT = (
        By.XPATH,
        (
            "//div[contains(@class, 'input_status_active')]"
            f"/input[@name='{ResetPasswordPageTexts.PASSWORD_INPUT_NAME}']"
        ),
    )
