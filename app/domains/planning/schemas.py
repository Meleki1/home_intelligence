from enum import Enum
from typing import Literal, Annotated, Union
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



"""class Plan(BaseModel):
    next_action: PlanAction
    priority: Priority
    missing_information: list[str] = []
    follow_up_questions: list[str] = []
    recommended_actions: list[str] = []
    safety_warnings: list[str] = []
    booking_reason: str | None = None
    explanation: str | None = None"""

class BasePlan(BaseModel):
    priority: Priority


class FollowUpPlan(BasePlan):

    next_action: Literal[PlanAction.ASK_FOLLOW_UP]

    missing_information: list[str]

    follow_up_questions: list[str]


class GuidancePlan(BasePlan):
    next_action: Literal[PlanAction.PROVIDE_GUIDANCE]
    recommended_actions: list[str]
    safety_warnings: list[str] = Field(default_factory=list)
    explanation: str

class BookingPlan(BasePlan):
    next_action: Literal[PlanAction.RECOMMEND_BOOKING]
    booking_reason: str
    explanation: str

class EmergencyPlan(BasePlan):
    next_action: Literal[PlanAction.EMERGENCY]
    safety_warnings: list[str]
    explanation: str

class OutOfScopePlan(BasePlan):
    next_action: Literal[PlanAction.OUT_OF_SCOPE]
    explanation: str


Plan = Annotated[
    Union[
        FollowUpPlan,
        GuidancePlan,
        BookingPlan,
        EmergencyPlan,
        OutOfScopePlan,
    ],
    Field(discriminator="next_action"),
]