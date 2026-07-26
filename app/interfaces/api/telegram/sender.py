from app.interfaces.api.telegram.client import TelegramClient


class TelegramSender:

    def __init__(self):

        self.client = TelegramClient()

    async def send_message(

        self,

        chat_id: int,

        text: str,

    ):

        await self.client.post(

            "sendMessage",

            {

                "chat_id": chat_id,

                "text": text,

            },

        )