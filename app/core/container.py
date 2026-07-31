from app.domains.AI.services.llm import LLMService
from app.domains.understanding.services.understanding import UnderstandingService
from app.domains.vision_analysis.service.vision_analysis import VisionService
from app.domains.conversation.services.state_service import ConversationStateService
from app.domains.conversation.services.fact_extractor.fact_extractor_service import FactExtractionService
from app.domains.conversation.services.cognition.processor import CognitiveProcessor
from app.domains.conversation.repository import ConversationRepository
from app.domains.AI.services.openai import OpenAIService
from app.domains.conversation.services.response_generator.service import ResponseGenerationService
from app.domains.planning.planner import PlannerService


class ServiceContainer:

    def __init__(self):

        self.openai_service = OpenAIService()

        self.llm_service = LLMService()

        self.vision_service = VisionService()

        self.planner = PlannerService(
            openai=self.openai_service
        )

        self.conversation_repository = ConversationRepository()

        self.conversation_service = ConversationStateService(
            repository=self.conversation_repository,
        )

        self.fact_extractor = FactExtractionService(
            openai=self.openai_service,
        )

        self.cognitive_processor = CognitiveProcessor(
            openai=self.openai_service,
        )

        self.response_generator = ResponseGenerationService(
            openai=self.openai_service,
        )

        

        self.understanding_service = UnderstandingService(
            conversation_service=self.conversation_service,
            fact_extractor=self.fact_extractor,
            cognitive_processor=self.cognitive_processor,
            planner=self.planner
        )