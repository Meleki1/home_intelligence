from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.timeline.schemas.timeline import CreateTimelineSchema
from app.core.events.base import BaseEvent
from app.domains.timeline.services.timeline_recording import TimelineRecordingService



class TimelineListener:

    def __init__(self, session:AsyncSession):

        self.service=(
            TimelineRecordingService(
                session
            )
        )

    async def listen(self, event:BaseEvent)->None:
        
        timeline=(
            CreateTimelineSchema(
                event_type=(
                    event.event_type
                ),

                event_name=(
                    event.event_name
                ),

                state=(
                    event.state
                ),

                description=(
                    event.description
                )

            )
        )

        try:
            await(
                self.service.record(
                    timeline
                )
            )
        except Exception:
            pass
