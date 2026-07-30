from pydantic import BaseModel, Field

class ExtractedFacts(BaseModel):

    affected_area: str | None = None
    duration: str | None = None
    occupants: str | None = None
    symptoms: list[str] = Field(default_factory=list)
    suspected_pest: str | None = None