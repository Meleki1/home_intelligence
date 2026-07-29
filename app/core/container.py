from app.domains.AI.services.llm import LLMService
from app.domains.understanding.services.understanding import UnderstandingService
from app.domains.vision_analysis.service.vision_analysis import VisionService
from app.domains.conversation.services.state_service import ConversationStateService
from app.domains.conversation.services.fact_extractor.fact_extractor_service import FactExtractionService
from app.domains.recommendations.services.recommendation import RecommendationService
from app.domains.decision.services.decision import DecisionService
from app.domains.conversation.services.cognition.processor import CognitiveProcessor
from app.domains.conversation.repository import ConversationRepository
from app.domains.AI.services.openai import OpenAIService

class ServiceContainer:

    def __init__(self):

        self.openai_service = OpenAIService()

        self.llm_service = LLMService()

        self.vision_service = VisionService()

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

        self.decision_service = DecisionService()

        self.recommendation_service = RecommendationService()

        self.understanding_service = UnderstandingService(
            conversation_service=self.conversation_service,
            fact_extractor=self.fact_extractor,
            recommendation_service=self.recommendation_service,
            decision_service=self.decision_service,
            cognitive_processor=self.cognitive_processor,
        )