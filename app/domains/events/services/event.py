from app.domains.events.schemas.event import EventSchema

class EventService:
    async def create(self, description:str)->EventSchema:
        return(
            EventSchema(
                description=description
            )
        )