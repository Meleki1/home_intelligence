from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class CreateServiceSchema(BaseModel):
    name:str
    description:str
    category:str

class ServiceResponseSchema(BaseModel):

    id:UUID
    name:str
    description:str
    category:str
    state:str
    created_at:datetime

    model_config=(
        ConfigDict(
            from_attributes=True
        )
    )