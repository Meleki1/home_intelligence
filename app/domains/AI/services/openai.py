import base64
from openai import AsyncOpenAI
from app.config.settings import get_settings
from app.domains.AI.builders.prompt_builder import build_prompt
from app.domains.AI.parsers.llm_response_parser import parse_response
from app.domains.AI.schemas.llm import LLMResponseSchema



class OpenAIService:
    def __init__(self):
        settings = get_settings()

        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate(self, prompt: str) -> LLMResponseSchema:

        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return parse_response(
            response.choices[0].message.content
        )
    
    async def generate_vision(self, prompt:str, image:bytes, mime_type:str) -> str:
        
        
        image_base64 = base64.b64encode(image).decode()

        response = await self.client.responses.create(
            model="gpt-5",
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
            

            
