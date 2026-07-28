from uuid import UUID
from pydantic import BaseModel
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse
from app.domains.conversation.models import ConversationState
from app.domains.decision.schemas.decision import DecisionSchema
from app.domains.conversation.services.cognition.schemas import CognitiveResult

class UnderstandingSchema(BaseModel):

    user_input: str
    image_analysis: VisionAnalysisResponse | None = None
    home_id: UUID | None = None
    conversation_id: str | None = None



class UnderstandingResult(BaseModel):

    state: ConversationState
    cognition: CognitiveResult
    decision: DecisionSchema
    recommendations: list[str]