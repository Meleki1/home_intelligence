from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.home.repositories.home_registration import HomeCreationRepository


class HomeService:

    def __init__(self, session:AsyncSession):
        self.repository = HomeCreationRepository(session)