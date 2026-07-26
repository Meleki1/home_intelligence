from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.services.models.service import Service
from app.domains.services.schemas.service import CreateServiceSchema
from app.domains.services.validators.service_creation import ServiceCreationValidator
from app.domains.services.repositories.service_creation import ServiceCreationRepository
from app.domains.services.events.service_created import ServiceCreatedEvent
from app.core.events.publisher import EventPublisher

class ServiceCreationService:
    def __init__(self, session:AsyncSession, publisher:EventPublisher):
        
        self.session=session

        self.publisher=publisher

        self.repository=ServiceCreationRepository(
            session
        )

    
    async def create_service(self, data:CreateServiceSchema)->Service:
        ServiceCreationValidator.validate(
            data
        )

        service=(
            Service(
                name=data.name,
                description=data.description,
                category=data.category
            )
        )

        try:
            service=(
                await(
                    self.repository.save(
                        service
                    )
                )
            )

            await(
                self.session.commit()
            )
        except Exception:

            await(
                self.session.rollback()
            )

            raise

        try:
            await(
                    self.publisher.publish(
                        ServiceCreatedEvent(
                            service.id
                        )
                    )
                )
        except Exception:   
            pass 

        return service

        

        