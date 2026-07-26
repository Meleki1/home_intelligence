from app.domains.chat.schemas.chat import ChatRequest

from .schemas import TelegramRequest


class TelegramParser:

    @staticmethod
    def parse(update: dict) -> TelegramRequest:

        message = update["message"]

        photo = message.get("photo")

        file_id = None

        if photo:
            # Telegram sends multiple image sizes.
            # The last one is the highest resolution.
            file_id = photo[-1]["file_id"]

        return TelegramRequest(

            chat_id=message["chat"]["id"],

            photo_file_id=file_id,

            request=ChatRequest(

                message=message.get("text", ""),

                conversation_id=str(
                    message["chat"]["id"]
                ),

            ),
        )