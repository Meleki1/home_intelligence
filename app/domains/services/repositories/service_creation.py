from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.services.models.service import Service

class ServiceCreationRepository:
    def __init__(self, session:AsyncSession):
        
        self.session=session

    async def save(self, service:Service)->Service:
        
        self.session.add(
            service
        )

        await(
            self.session.flush()
        )

        await(
            self.session.refresh(
                service
            )
        )

        return service