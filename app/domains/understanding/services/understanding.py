from app.domains.understanding.schemas.understanding import UnderstandingSchema
from app.domains.conversation.services.state_service import ConversationStateService
from app.domains.recommendations.services.recommendation import RecommendationService
from app.domains.decision.services.decision import DecisionService
from app.domains.conversation.services.fact_extractor.fact_extractor_service import FactExtractionService
from app.domains.understanding.schemas.understanding import UnderstandingResult
from app.domains.conversation.services.cognition.processor import CognitiveProcessor


class UnderstandingService:

    def __init__(
        self,
        conversation_service: ConversationStateService,
        fact_extractor: FactExtractionService,
        recommendation_service: RecommendationService,
        decision_service: DecisionService,
        cognitive_processor: CognitiveProcessor
    ):

        self.conversation_service = conversation_service
        self.fact_extractor = fact_extractor
        self.recommendation_service = recommendation_service
        self.decision_service = decision_service
        self.cognitive_processor = cognitive_processor
        
    async def understand(self, data: UnderstandingSchema):
        
        state = await self.conversation_service.load(
            data.conversation_id
        )
        
        facts = await self.fact_extractor.extract(
            data.user_input
        )

        await self.conversation_service.merge_facts(
            state,
            facts,
        )

        if data.image_analysis:

            await self.conversation_service.merge_image(
                state,
                data.image_analysis,
            )

        missing = (
            await self.conversation_service.compute_missing(
                state
            )
        )
        
        cognition = await self.cognitive_processor.process(
            state,
            missing,
        )

        state.cognition = cognition

        await self.conversation_service.save(
            state
        )

        decision = await self.decision_service.decide(

            state,

            cognition,
        )

        recommendations = (
            await self.recommendation_service.recommend(

                state,
                cognition,
                decision,
            )
        )

        return UnderstandingResult(

            state=state,
            cognition=cognition,
            decision=decision,
            recommendations=recommendations,
        )
            


       
        
        
        
        
        
 
        
        
        






"""class UnderstandingService:

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

"""