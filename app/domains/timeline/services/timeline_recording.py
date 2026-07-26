from sqlalchemy.ext.asyncio import AsyncSession
from app.domains.timeline.repositoies.timeline_creation import TimelineCreationRepositoy
from app.core.events.publisher import EventPublisher
from app.domains.timeline.schemas.timeline import CreateTimelineSchema
from app.domains.timeline.model.timeline import Timeline
from app.domains.timeline.validator.timeline_creation import TimelineCreationValidator


class TimelineRecordingService:
    def __init__(self, session:AsyncSession):
        self.session = session

        self.repository=(
            TimelineCreationRepositoy(
                session
            )
        )

        """self.publisher=(
            EventPublisher()
        )"""

    async def record(self, data:CreateTimelineSchema)->Timeline:

        TimelineCreationValidator.validate(
            data
        )

        timeline = Timeline(
            event_type=data.event_type,
            event_name=data.event_name,
            state=data.state,
            description=data.description
        )

        try:
            timeline=(
                await(
                    self.repository.save(
                        timeline
                    )
                )
            )

            await(
                self.session.commit()
            )

            return timeline

        except Exception:
            await(
                self.session.rollback()
            )

            raise