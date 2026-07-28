from uuid import UUID
from .models import ConversationState


class ConversationRepository:

    def __init__(self):

        self.storage: dict[UUID, ConversationState] = {}

    async def get(
        self,
        conversation_id: UUID,
    ) -> ConversationState | None:

        return self.storage.get(conversation_id)

    async def save(
        self,
        state: ConversationState,
    ):

        self.storage[state.conversation_id] = state