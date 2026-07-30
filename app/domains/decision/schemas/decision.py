from pydantic import BaseModel, Field


class DecisionSchema(BaseModel):

    next_action: str
    missing_information: list[str] = Field(default_factory=list)