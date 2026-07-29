from app.domains.recommendations.schemas.recommendation import RecommendationSchema
from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import CognitiveResult
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
                title="More Information Required",
                description=(
                    "Additional information is needed "
                    "before a recommendation can be made."
                ),
                priority="MEDIUM",
                category="FOLLOW_UP",
            )

        if decision.next_action == "REQUEST_IMAGE":
            return RecommendationSchema(
                title="Image Required",
                description=(
                    "Please upload a clear photo so the "
                    "system can identify the issue."
                ),
                priority="HIGH",
                category="FOLLOW_UP",
            )

        if decision.next_action == "PROVIDE_RECOMMENDATION":
            return RecommendationSchema(
                title="Recommendation Ready",
                description=cognition.summary,
                priority="MEDIUM",
                category="SELF_HELP",
            )

        if decision.next_action == "BOOK_EXPERT":
            return RecommendationSchema(
                title="Professional Assistance Recommended",
                description=(
                    "The issue appears significant enough "
                    "to recommend booking a pest control expert."
                ),
                priority="HIGH",
                category="BOOKING",
            )

        return RecommendationSchema(
            title="Continue Conversation",
            description=cognition.next_best_step,
            priority="LOW",
            category="FOLLOW_UP",
        )
