from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import CognitiveResult
from app.domains.decision.schemas.decision import DecisionSchema


class DecisionService:

    async def decide(
        self,
        state: ConversationState,
        cognition: CognitiveResult,
    ) -> DecisionSchema:

        missing = []

        if not state.image_received:
            missing.append("image")

        if not state.affected_area:
            missing.append("affected_area")

        if not state.duration:
            missing.append("duration")

        if missing:

            # If an image is missing, prioritize requesting it.
            if "image" in missing:
                return DecisionSchema(
                    next_action="REQUEST_IMAGE",
                    missing_information=missing,
                )

            return DecisionSchema(
                next_action="ASK_FOLLOW_UP",
                missing_information=missing,
            )

        if cognition.confidence == "LOW":

            return DecisionSchema(
                next_action="BOOK_EXPERT",
            )

        return DecisionSchema(
            next_action="PROVIDE_RECOMMENDATION",
        )