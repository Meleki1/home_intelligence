from pydantic import BaseModel, Field
from enum import Enum


class Confidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"



class VisionAnalysisSchema(BaseModel):
    description: str
    objects: list[str]

class VisionAnalysisResponse(BaseModel):
    summary: str
    confidence: Confidence
    detected_objects: list[str] = Field(default_factory=list)
    observations: list[str] = Field(default_factory=list)
    possible_issue:str | None
    recommendations: list[str] = Field(default_factory=list)
    requires_professional: bool


