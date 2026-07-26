from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.timeline.model.timeline import Timeline

class TimelineCreationRepositoy:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def save(self, timeline:Timeline)->Timeline:
        
        self.session.add(timeline)

        await self.session.flush()

        await self.session.refresh(timeline)

        return timeline

