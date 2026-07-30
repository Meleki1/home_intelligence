from pydantic import BaseModel
from typing import Literal 

from pydantic import BaseModel, Field


class RecommendationSchema(BaseModel):

    action: str

    follow_up_fields: list[str] = Field(default_factory=list)

    priority: str

    category: str