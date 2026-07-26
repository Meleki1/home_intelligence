from pydantic import BaseModel


class ChatSchema(BaseModel):
    message: str
    conversation_id: str | None = None
    home_id: str | None = None


class ResponseSchema(BaseModel):
    message: str
    intent: str
    confidence: str
    next_best_step: str | None = None
    conversation_id: str | None = None


from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None
    home_id: str | None = None


"""from typing import Annotated

from pydantic import BaseModel, Field, AliasChoices
from app.domains.chat.enums.next_best_step import NextBestStep

class ChatSchema(BaseModel):

    message: Annotated[
        str,
        Field(
            validation_alias=AliasChoices(
                "message",
                "user_input",
            )
        ),
    ]
    image: bytes
    mime_type: str
    conversation_id: str | None = None
    home_id: str | None = None


class ResponseSchema(BaseModel):
    message: str
    intent:str
    confidence:str
    next_best_step: str | None = None
    conversation_id: str | None = None
"""