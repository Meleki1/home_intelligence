from app.domains.AI.services.llm import LLMService
from app.domains.understanding.services.understanding import UnderstandingService
from app.domains.vision_analysis.service.vision_analysis import VisionService
from app.domains.conversation.services.state_service import ConversationStateService
from app.domains.conversation.services.fact_extractor.fact_extractor_service import FactExtractionService
from app.domains.recommendations.services.recommendation import RecommendationService
from app.domains.decision.services.decision import DecisionService
from app.domains.conversation.services.cognition.processor import CognitiveProcessor


class ServiceContainer:

    def __init__(self):

        self.llm = LLMService()
        self.vision = VisionService()

        self.conversation = ConversationStateService()
        self.fact_extractor = FactExtractionService()

        self.cognitive = CognitiveProcessor()

        self.decision = DecisionService()

        self.recommendation = RecommendationService()

        self.understanding = UnderstandingService(
            conversation_service=self.conversation,
            fact_extractor=self.fact_extractor,
            recommendation_service=self.recommendation,
            decision_service=self.decision,
            cognitive_processor=self.cognitive,
        )