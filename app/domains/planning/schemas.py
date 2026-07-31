from enum import Enum
from pydantic import BaseModel, Field


class PlanAction(str, Enum):
    ASK_FOLLOW_UP = "ASK_FOLLOW_UP"
    PROVIDE_GUIDANCE = "PROVIDE_GUIDANCE"
    RECOMMEND_BOOKING = "RECOMMEND_BOOKING"
    ESCALATE = "ESCALATE"
    EMERGENCY = "EMERGENCY"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    EMERGENCY = "EMERGENCY"

class PlannerConfidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Plan(BaseModel):
    next_action: PlanAction
    priority: Priority
    planner_confidence: PlannerConfidence
    missing_information: list[str] = Field(default_factory=list)
    follow_up_questions: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    safety_warnings: list[str] = Field(default_factory=list)
    booking_reason: str | None = None
    explanation: str

