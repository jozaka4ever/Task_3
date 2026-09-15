class Urls:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_PAGE = f"{BASE_URL}/account/order-history"
    ORDER_FEED_PAGE = f"{BASE_URL}/feed"
    INGREDIENT_DETAILS_PREFIX = f"{BASE_URL}/ingredient/"
    ORDER_DETAILS_PREFIX = f"{ORDER_FEED_PAGE}/"

    REGISTER_USER_API = f"{BASE_URL}/api/auth/register"
    USER_API = f"{BASE_URL}/api/auth/user"
