from pydantic import BaseModel

class RecommendationSchema(BaseModel):
    title:str
    description:str