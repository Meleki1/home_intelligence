from app.domains.understanding.schemas.understanding import (
    UnderstandingSchema,
)

from app.domains.understanding.processors.current_hypothesis import (
    CurrentHypothesisProcessor,
)

from app.domains.understanding.processors.current_knowledge import (
    CurrentKnowledgeProcessor,
)

from app.domains.understanding.processors.summaries import (
    SummaryProcessor,
)

from app.domains.understanding.processors.unknown_context import (
    UnknownContextProcessor,
)

from app.domains.understanding.processors.next_best_step import (
    NextBestStepProcessor,
)

from app.domains.recommendations.services.recommendation import (
    RecommendationService,
)

from app.domains.decision.services.decision import (
    DecisionService,
)


class UnderstandingService:

    def __init__(self):

        self.recommendation_service = (
            RecommendationService()
        )

        self.decision_service = (
            DecisionService()
        )

    async def understand(
        self,
        data: UnderstandingSchema,
    ):

        image_uploaded = (
            data.image_analysis is not None
        )

        decision = await self.decision_service.decide(
            image_uploaded=image_uploaded
        )

        recommendations = (
            await self.recommendation_service.recommend(
                user_input=data.user_input,
                image_uploaded=image_uploaded,
            )
        )

        return {

            "user_input": data.user_input,

            "current_hypothesis":
            await CurrentHypothesisProcessor.process(),

            "current_knowledge":
            await CurrentKnowledgeProcessor.process(
                data.user_input
            ),

            "unknown_context":
            await UnknownContextProcessor.process(
                data.user_input
            ),

            "next_best_step":
            await NextBestStepProcessor.process(
                data.user_input
            ),

            "summary":
            await SummaryProcessor.process(),

            "decision":
            decision,

            "recommendations":
            recommendations,

            "image_analysis":
            data.image_analysis,

        }

"""class NextAction(Enum):

    CONTINUE_CONVERSATION=(
        "CONTINUE_CONVERSATION"
    )

    UPLOAD_IMAGE=(
        "UPLOAD_IMAGE"
    )

    MONITOR_ISSUE=(
        "MONITOR_ISSUE"
    )

    PROFESSIONAL_ASSISTANCE=(

        "PROFESSIONAL_ASSISTANCE"

    )

    ISSUE_RESOLVED=(
        "ISSUE_RESOLVED"
    )"""