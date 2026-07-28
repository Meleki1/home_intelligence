from pydantic import BaseModel, Field
from uuid import UUID


class ConversationState(BaseModel):
    conversation_id: UUID

    # Facts extracted from the user
    affected_area: str | None = None
    duration: str | None = None
    occupants: str | None = None
    symptoms: list[str] = Field(default_factory=list)

    # Vision
    image_received: bool = False
    image_summary: str | None = None

    # Pest
    suspected_pest: str | None = None
    confidence: str | None = None

    # Conversation
    summary: str = ""

    # Internal tracking
    completed_questions: set[str] = Field(default_factory=set)