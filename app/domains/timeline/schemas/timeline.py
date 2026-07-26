from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict



class CreateTimelineSchema(BaseModel):

    event_type:str
    event_name:str
    state:str
    description:str

class TimelineResponseSchema(BaseModel):
    
    id:UUID
    event_type:str
    event_name:str
    state:str
    description:str
    created_at:datetime

    model_config=(
        ConfigDict(
            from_attributes=True
        )
    )

