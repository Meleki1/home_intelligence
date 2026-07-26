from pydantic import BaseModel
from pydantic import Field

class HomeInformationSchema(BaseModel):
    country:str
    city:str
    address:str
    zipcode:str | None = None

class CreateHomeSchema(BaseModel):
    name:str = Field(
        min_length=3,
        max_length=150
    )

    home_type:str
    description:str | None = None
    
    information:HomeInformationSchema

class HomeInformationResponse(BaseModel):
    country:str
    city:str
    address:str
    zipcode:str | None = None


class HomeResponseSchema(BaseModel):
    id:str
    name:str
    home_type:str
    description:str
    status:str

    information:(HomeInformationResponse)

class HomeCreationResponse(BaseModel):
    success:bool
    message:str

    home:(HomeResponseSchema | None)