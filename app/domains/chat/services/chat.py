from uuid import UUID
from app.domains.AI.services.llm import LLMService
from app.domains.chat.builders.response_builder import  build_response, resolve_next_best_step, SIMPLE_INTENTS
from app.domains.chat.schemas.chat import ChatRequest, ResponseSchema
from app.domains.understanding.schemas.understanding import UnderstandingSchema
from app.domains.understanding.services.understanding import UnderstandingService
from app.domains.vision_analysis.service.vision_analysis import VisionService
from app.interfaces.api.telegram.schemas import ImageInput
from app.domains.conversation.services.state_service import ConversationStateService
from app.domains.conversation.services.fact_extractor.fact_extractor_service import FactExtractionService
from app.domains.recommendations.services.recommendation import RecommendationService
from app.domains.decision.services.decision import DecisionService
from app.domains.conversation.services.cognition.processor import CognitiveProcessor
from app.core.container import ServiceContainer

class ChatService:

    def __init__(self):

        container = ServiceContainer()

        self.llm_service = container.llm
        self.vision_service = container.vision
        self.understanding_service = container.understanding

    async def chat(
        self,
        request: ChatRequest,
        image: ImageInput | None = None,
    ) -> ResponseSchema:

        image_analysis = None

        if image is not None:

            image_analysis = (
                await self.vision_service.analyze(
                    image=image.data,
                    mime_type=image.mime_type,
                )
            )



        understanding = (
            await self.understanding_service.understand(
                UnderstandingSchema(
                    user_input=request.message,
                    image_analysis=image_analysis,
                    home_id=(
                        UUID(request.home_id)
                        if request.home_id
                        else None
                    ),
                    conversation_id=request.conversation_id,
                )
            )
        )

        llm_response = await self.llm_service.generate(
            understanding
        )

        message = build_response(
            llm_response,
            understanding,
        )

        next_best_step = (
            None
            if llm_response.intent in SIMPLE_INTENTS
            else resolve_next_best_step(
                understanding
            )
        )

        return ResponseSchema(
            message=message,
            intent=llm_response.intent,
            confidence=llm_response.confidence,
            next_best_step=next_best_step,
            conversation_id=request.conversation_id,
        )