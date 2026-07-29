from uuid import UUID

from app.domains.conversation.models import ConversationState


class ConversationRepository:

    def __init__(self):

        self._storage: dict[
            UUID,
            ConversationState,
        ] = {}

    async def get(
        self,
        conversation_id: UUID,
    ) -> ConversationState | None:

        return self._storage.get(
            conversation_id
        )

    async def save(
        self,
        state: ConversationState,
    ) -> None:

        self._storage[
            state.conversation_id
        ] = state

    async def delete(
        self,
        conversation_id: UUID,
    ) -> None:

        self._storage.pop(
            conversation_id,
            None,
        )

    async def exists(
        self,
        conversation_id: UUID,
    ) -> bool:

        return (
            conversation_id
            in self._storage
        )

    async def list(
        self,
    ) -> list[ConversationState]:

        return list(
            self._storage.values()
        )