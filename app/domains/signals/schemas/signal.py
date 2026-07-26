from pydantic import BaseModel

class SignalSchema(BaseModel):
    signal_type:str
    value:str