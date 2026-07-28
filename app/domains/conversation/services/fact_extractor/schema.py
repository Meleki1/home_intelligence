from pydantic import BaseModel

class ExtractedFacts(BaseModel):

    affected_area: str | None = None

    duration: str | None = None

    occupants: str | None = None

    symptoms: list[str] = []

    pest: str | None = None