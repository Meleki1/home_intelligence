from pydantic import BaseModel


class DecisionSchema(BaseModel):

    next_action:str

    reason:str