from app.domains.home.models.home_state import HomeState


class HomeStateRepository():
    async def save_state(self, state:HomeState):
        self.session.add(state)