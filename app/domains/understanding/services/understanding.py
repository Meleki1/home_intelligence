from app.domains.understanding.schemas.understanding import (
    UnderstandingSchema,
    UnderstandingResult,
)
from app.domains.conversation.services.state_service import (
    ConversationStateService,
)
from app.domains.conversation.services.fact_extractor.fact_extractor_service import (
    FactExtractionService,
)
from app.domains.conversation.services.cognition.processor import (
    CognitiveProcessor,
)
from app.domains.planning.planner import PlannerService


class UnderstandingService:

    def __init__(
        self,
        conversation_service: ConversationStateService,
        fact_extractor: FactExtractionService,
        cognitive_processor: CognitiveProcessor,
        planner: PlannerService,
    ):
        self.conversation_service = conversation_service
        self.fact_extractor = fact_extractor
        self.cognitive_processor = cognitive_processor
        self.planner = planner

    async def understand(
        self,
        data: UnderstandingSchema,
    ) -> UnderstandingResult:

        conversation_id = data.conversation_id or "default"

        state = await self.conversation_service.load(
            conversation_id
        )

        facts = await self.fact_extractor.extract(
            data.user_input
        )
        print("Extracted facts:", facts.model_dump())

        await self.conversation_service.merge_facts(
            state,
            facts,
        )
        print("State after merge:", state.model_dump())
        if data.image_analysis:
            await self.conversation_service.merge_image(
                state,
                data.image_analysis,
            )

        missing = await self.conversation_service.compute_missing(
            state
        )
        print(missing)

        cognition = await self.cognitive_processor.process(
            state,
            missing,
        )
        print("Cognition:", cognition.model_dump())


        state.cognition = cognition

        plan = await self.planner.plan(
            state=state,
            cognition=cognition,
        )
        print("\n========== PLAN ==========")
        print(plan.model_dump())
        print("==========================\n")

        await self.conversation_service.save(
            state
        )

        return UnderstandingResult(
            user_input=data.user_input,
            image_analysis=data.image_analysis,
            state=state,
            cognition=cognition,
            plan=plan,
        )