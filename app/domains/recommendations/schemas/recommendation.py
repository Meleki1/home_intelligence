from pydantic import BaseModel
from typing import Literal 

class RecommendationSchema(BaseModel):

    title: str

    description: str

    priority: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ]

    category: Literal[
        "FOLLOW_UP",
        "SELF_HELP",
        "BOOKING",
        "SAFETY",
    ]