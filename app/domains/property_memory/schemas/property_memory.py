from uuid import UUID
from pydantic import BaseModel

class PropertyMemoySchema(BaseModel):

    home_id: UUID
    memory: str