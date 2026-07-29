from pydantic import BaseModel


class CognitiveResult(BaseModel):

    current_knowledge: str
    current_hypothesis: str
    summary: str
    next_best_step: str
    reasoning: str
    confidence: str
