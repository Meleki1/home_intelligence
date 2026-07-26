from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class BaseEvent:
    event_type: str
    event_name: str
    state: str
    description: str
    created_at: datetime | None = None
    resource_id: UUID    |  None=None