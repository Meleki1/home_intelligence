from app.domains.AI.builders.prompt_builder import build_prompt
from app.domains.AI.services.openai import OpenAIService
from app.domains.AI.schemas.llm import LLMResponseSchema

class LLMService:

    def __init__(self):
        self.openai_service = OpenAIService()

    async def generate(self, understanding) -> LLMResponseSchema:

        prompt = build_prompt(understanding)

        return await self.openai_service.generate(prompt)