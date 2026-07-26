class InvalidServiceNameException(Exception):
    def __init__(self):
        super().__init__(
            "Service name cannot be empty"
        )

class InvalidServiceDescriptionException(Exception):
    def __init__(self):
        super().__init__(
            "Service description cannot be empty"
        )

class InvalidServiceCategoryException(Exception):
    def __init__(self):
        super().__init__(
            "Service category cannot be empty"
        )