from enum import Enum
from pydantic import BaseModel, Field


class PlanAction(str, Enum):
    ASK_FOLLOW_UP = "ASK_FOLLOW_UP"
    PROVIDE_GUIDANCE = "PROVIDE_GUIDANCE"
    BOOK_EXPERT = "BOOK_EXPERT"
    ESCALATE = "ESCALATE"


class Plan(BaseModel):
    next_action: PlanAction
    missing_information: list[str] = Field(default_factory=list)
    follow_up_questions: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    recommend_booking: bool = False
    priority: str = "MEDIUM"