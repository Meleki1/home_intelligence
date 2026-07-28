from uuid import UUID
from pydantic import BaseModel
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse
from app.domains.conversation.models import ConversationState

class UnderstandingSchema(BaseModel):

    user_input: str
    image_analysis: VisionAnalysisResponse | None = None
    home_id: UUID | None = None
    conversation_id: str | None = None



class UnderstandingResult(BaseModel):

    state: ConversationState

    missing_information: list[str]

    current_hypothesis: str

    next_best_step: str

    recommendations: list[str]