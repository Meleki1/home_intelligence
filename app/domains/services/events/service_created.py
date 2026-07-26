from uuid import UUID
from app.core.events.base import BaseEvent

class ServiceCreatedEvent(BaseEvent):
    def __init__(self, service_id:UUID):
        super().__init__(
            event_type="SERVICE",
            event_name="SERVICE_CREATED",
            state="SUCCESS",
            description=(
                "Service created successfully."
            ),
            resource_id=(
                service_id
            )
        )