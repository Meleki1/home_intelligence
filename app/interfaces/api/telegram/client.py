import httpx

from app.config.settings import get_settings


class TelegramClient:

    def __init__(self):

        settings = get_settings()

        self.base_url = (
            f"https://api.telegram.org/bot"
            f"{settings.TELEGRAM_BOT_TOKEN}"
        )

    async def post(
        self,
        method: str,
        payload: dict,
    ):

        async with httpx.AsyncClient() as client:

            response = await client.post(

                f"{self.base_url}/{method}",

                json=payload,

            )

            response.raise_for_status()

            return response.json()