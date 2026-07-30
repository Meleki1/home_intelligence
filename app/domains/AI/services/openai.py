import base64
from openai import AsyncOpenAI
from app.config.settings import get_settings
from app.domains.AI.builders.prompt_builder import build_prompt
from app.domains.AI.parsers.llm_response_parser import parse_response
from app.domains.AI.schemas.llm import LLMResponseSchema
from pydantic import BaseModel


class OpenAIService:

    def __init__(self):
        settings = get_settings()

        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_text(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str = "gpt-4o-mini",
    ) -> str:

        response = await self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.choices[0].message.content

    async def generate_json(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel],
        model: str = "gpt-4o-mini",
    ) -> BaseModel:

        response = await self.client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            response_format=response_model,
        )

        return response.choices[0].message.parsed

    async def generate_vision(
        self,
        prompt: str,
        image: bytes,
        mime_type: str,
        model: str = "gpt-4o-mini",
    ) -> str:

        image_base64 = base64.b64encode(image).decode()

        response = await self.client.responses.create(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt,
                        },
                        {
                            "type": "input_image",
                            "image_url": (
                                f"data:{mime_type};base64,{image_base64}"
                            ),
                        },
                    ],
                }
            ],
        )

        return response.output_text
            

            
