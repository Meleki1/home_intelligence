from app.domains.home.constants import HOME_TYPES
from app.domains.home.exceptions import InvalidHomeTypeException


class HomeCreationValidator:
    @staticmethod
    def validate_home_type(home_type: str):
        if home_type.lower() not in HOME_TYPES:
            raise InvalidHomeTypeException(f"{home_type} is not supported.")
