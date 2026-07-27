from fastapi import APIRouter
from fastapi import Request

from app.domains.chat.schemas.chat import ChatRequest
from app.domains.chat.services.chat import ChatService
from app.interfaces.api.telegram.sender import TelegramSender
from app.interfaces.api.telegram.parser import TelegramParser
from pydantic import BaseModel
from app.domains.chat.schemas.chat import ChatRequest
from app.interfaces.api.telegram.downloader import TelegramDownloader
from app.interfaces.api.telegram.schemas import ImageInput

class TelegramRequest(BaseModel):
    chat_id: int
    request: ChatRequest

router = APIRouter()

chat_service = ChatService()
sender = TelegramSender()
downloader = TelegramDownloader()


@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):

    update = await request.json()

    telegram = TelegramParser.parse(update)

    image_input = None

    if telegram.photo_file_id:

        data, mime = await downloader.download(
            telegram.photo_file_id
        )

        image_input = ImageInput(
            data=data,
            mime_type=mime,
        )

    response = await chat_service.chat(
        request=telegram.request,
        image=image_input,
    )

    await sender.send_message(
        telegram.chat_id,
        response.message,
    )

    return {"ok": True}