from app.domains.services.schemas.service import CreateServiceSchema
from app.domains.services.exceptions.service import InvalidServiceNameException
from app.domains.services.exceptions.service import InvalidServiceDescriptionException
from app.domains.services.exceptions.service import InvalidServiceCategoryException


class ServiceCreationValidator:

    @staticmethod
    def validate(data:CreateServiceSchema)->None:
        ServiceCreationValidator.validate_name(
            data.name
        )

        ServiceCreationValidator.validate_description(
            data.description
        )

        ServiceCreationValidator.validate_category(
            data.category
        )

    @staticmethod
    def validate_name(name:str)->None:
        if not name.strip():
            raise(
                InvalidServiceNameException
            )

    @staticmethod
    def validate_description(description:str)->None:
        if not description.strip():
            raise(
                InvalidServiceDescriptionException
            )

    @staticmethod
    def validate_category(category:str)->None:
        if not category.strip():
            raise(
                InvalidServiceCategoryException
            )