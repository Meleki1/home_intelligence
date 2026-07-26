from uuid import UUID
from pydantic import BaseModel
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse

class UnderstandingSchema(BaseModel):

    user_input: str
    image_analysis: VisionAnalysisResponse | None = None
    home_id: UUID | None = None
    conversation_id: str | None = None


from pydantic import BaseModel

class UnderstandingResult(BaseModel):

    user_input: str

    current_hypothesis: str

    current_knowledge: str

    unknown_context: str

    next_best_step: str

    summary: str

    decision: str

    recommendations: list[str]

    image_analysis: VisionAnalysisResponse | None = None