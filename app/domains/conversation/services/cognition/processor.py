from app.domains.AI.services.openai import OpenAIService
from .schemas import CognitiveResult
from .prompt import COGNITIVE_PROMPT
import json


class CognitiveProcessor:

    def __init__(self, openai: OpenAIService):
        self.openai = openai

    async def process(
        self,
        state,
        missing_information,
    ) -> CognitiveResult:

        context = json.dumps(
            {
                "state": state.model_dump(),
                "missing_information": missing_information,
            },
            indent=2,
        )

        return await self.openai.generate_json(
            system_prompt=COGNITIVE_PROMPT,
            user_prompt=context,
            response_model=CognitiveResult,
        )