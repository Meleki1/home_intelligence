from app.core.exceptions.business import BusinessException

class InvalidHomeTypeException(BusinessException):
    pass


class HomeAlreadyExistsException(BusinessException):
    pass


class InvalidAddressException(BusinessException):
    pass