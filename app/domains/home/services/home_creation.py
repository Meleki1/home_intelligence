from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.home.models.home import Home
from app.domains.home.models.home_state import HomeState
from app.domains.home.models.home_information import HomeInformation
from app.domains.home.repositories.home_registration import HomeCreationRepository
from app.domains.home.schemas.home_creation import CreateHomeSchema
from app.core.events.publisher import EventPublisher
from app.domains.home.events import HomeCreatedEvent
from app.domains.home.validators.home_creation import HomeCreationValidator

class HomeCreationService:

    def __init__(self, session:AsyncSession, publisher):

        self.session = session

        

        self.repository = (
            HomeCreationRepository(
                session
            )
        )

        self.publisher=(
            publisher
        )

        self.validator = HomeCreationValidator()




    async def create_home(
        self,
        data: CreateHomeSchema
    ):
        self.validator.validate_home_type(
                data.home_type
            )
            
        try:

            

            home = Home(
                name=data.name,
                home_type=data.home_type,
                description=data.description
            )

            home = await (
                self.repository.save_home(
                    home
                )
            )

            information = (
                HomeInformation(
                    home_id=home.id,
                    country=data.information.country,
                    city=data.information.city,
                    address=data.information.address,
                    Zipcode=data.information.zipcode
                )
            )

            await self.repository.save_information(
                information
            )

            state = HomeState(
                home_id=home.id
            )

            await self.repository.save_state(
                state
            )

            await self.session.commit()

            event = HomeCreatedEvent(
                home.id
            )

            await (
                self.publisher.publish(
                    event
                )
            )

            return home

        except Exception as error:
            await self.session.rollback()
            raise error
    
    
    