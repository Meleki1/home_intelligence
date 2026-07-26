from datetime import datetime, timezone
from uuid import UUID
from app.core.events.base import BaseEvent
from dataclasses import dataclass

@dataclass
class HomeCreatedEvent(BaseEvent):
    def __init__(self, home_id:UUID):
        super().__init__(
            event_type="HOME",
            event_name="HomeCreated",
            state="SUCCESS",
            description=(
                "Home created successfully"
            ),
            created_at=datetime.now(
                timezone.utc
            ),
            resource_id=(
                home_id
            )
        )

        