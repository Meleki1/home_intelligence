from pydantic import BaseModel

from app.domains.chat.schemas.chat import ChatRequest


class TelegramRequest(BaseModel):

    chat_id: int

    request: ChatRequest

    photo_file_id: str | None = None
    




class ImageInput(BaseModel):

    data: bytes
    mime_type: str
    filename: str | None = None
    source: str | None = None