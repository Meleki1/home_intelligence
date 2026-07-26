from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.home.models.home import Home
from app.domains.home.models.home_information import HomeInformation
from app.domains.home.models.home_state import HomeState


class HomeCreationRepository:
    def __init__(
        self,
        session: AsyncSession
    ):

        self.session = session

    async def save_home(self, home: Home) -> Home:

        self.session.add(home)

        await self.session.flush()

        await self.session.refresh(home)

        return home

    async def save_information(self, information: HomeInformation):
        self.session.add(information)

    async def save_state(self, state: HomeState):
        self.session.add(state)
