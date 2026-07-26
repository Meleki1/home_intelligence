from pydantic import BaseModel


class LLMResponseSchema(BaseModel):

    intent:str
    signals:list[str]
    summary:str
    confidence:str
    