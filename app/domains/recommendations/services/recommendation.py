from app.domains.recommendations.schemas.recommendation import (
    RecommendationSchema,
)
from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import (
    CognitiveResult,
)
from app.domains.decision.schemas.decision import DecisionSchema


class RecommendationService:

    async def recommend(
        self,
        state: ConversationState,
        cognition: CognitiveResult,
        decision: DecisionSchema,
    ) -> RecommendationSchema:

        if decision.next_action == "ASK_FOLLOW_UP":

            return RecommendationSchema(
                action="ASK_FOLLOW_UP",
                follow_up_fields=decision.missing_information,
                priority="MEDIUM",
                category="FOLLOW_UP",
            )

        if decision.next_action == "REQUEST_IMAGE":

            return RecommendationSchema(
                action="REQUEST_IMAGE",
                follow_up_fields=["image"],
                priority="HIGH",
                category="FOLLOW_UP",
            )

        if decision.next_action == "PROVIDE_RECOMMENDATION":

            return RecommendationSchema(
                action="PROVIDE_RECOMMENDATION",
                priority="MEDIUM",
                category="SELF_HELP",
            )

        if decision.next_action == "BOOK_EXPERT":

            return RecommendationSchema(
                action="BOOK_EXPERT",
                priority="HIGH",
                category="BOOKING",
            )

        return RecommendationSchema(
            action="CONTINUE_CONVERSATION",
            priority="LOW",
            category="FOLLOW_UP",
        )