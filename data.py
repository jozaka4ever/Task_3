from uuid import uuid4


class UserTestData:
    @staticmethod
    def generate_user():
        suffix = uuid4().hex
        return {
            "email": f"qa-ui-{suffix}@example.com",
            "password": f"QaPassword-{suffix}",
            "name": f"QA User {suffix[:8]}",
        }

    @staticmethod
    def generate_email():
        return f"qa-recovery-{uuid4().hex}@example.com"


class IngredientTestData:
    BUN_NAME = "Краторная булка N-200i"
    SAUCE_NAME = "Соус Spicy-X"
