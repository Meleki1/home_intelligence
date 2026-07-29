from app.domains.AI.services.openai import OpenAIService

from .schemas import CognitiveResult

from .prompt import COGNITIVE_PROMPT


class CognitiveProcessor:

    def __init__(self, openai: OpenAIService):

        self.openai = openai

    async def process(self, state, missing_information):

        response = await self.openai.generate_json(

            prompt=COGNITIVE_PROMPT,

            state=state.model_dump(),

            missing_information=missing_information,
        )
        return CognitiveResult.model_validate_json(
            response
        )