from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import CognitiveResult
from app.domains.decision.schemas.decision import DecisionSchema


class DecisionService:

    async def decide(
        self,
        state: ConversationState,
        cognition: CognitiveResult,
    ) -> DecisionSchema:

        if not state.image_received:
            return DecisionSchema(
                next_action="REQUEST_IMAGE",
                reason=(
                    "A clear photo would help identify the issue "
                    "before making a recommendation."
                ),
            )

        if not state.affected_area or not state.duration:
            return DecisionSchema(
                next_action="ASK_FOLLOW_UP",
                reason=(
                    "Additional details about the affected area and "
                    "how long the issue has been present are needed."
                ),
            )

        if cognition.confidence == "LOW":
            return DecisionSchema(
                next_action="BOOK_EXPERT",
                reason=(
                    "Confidence is low and a professional inspection "
                    "is recommended."
                ),
            )

        return DecisionSchema(
            next_action="PROVIDE_RECOMMENDATION",
            reason=(
                "Enough information is available to provide guidance."
            ),
        )
