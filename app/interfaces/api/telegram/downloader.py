import httpx

from app.config.settings import get_settings


class TelegramDownloader:

    def __init__(self):

        settings = get_settings()

        self.token = settings.TELEGRAM_BOT_TOKEN

    async def download(
        self,
        file_id: str,
    ) -> tuple[bytes, str]:

        async with httpx.AsyncClient() as client:

            file = await client.get(

                f"https://api.telegram.org/bot{self.token}/getFile",

                params={
                    "file_id": file_id,
                },

            )

            file.raise_for_status()

            file_path = file.json()["result"]["file_path"]

            image = await client.get(

                f"https://api.telegram.org/file/bot{self.token}/{file_path}"

            )

            image.raise_for_status()

            return image.content, "image/jpeg"