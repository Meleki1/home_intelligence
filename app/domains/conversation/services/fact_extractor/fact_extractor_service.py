from app.domains.conversation.services.fact_extractor.prompt import FACT_EXTRACTION_PROMPT
from app.domains.conversation.services.fact_extractor.schema import ExtractedFacts
from app.domains.AI.services.openai import OpenAIService


class FactExtractionService:

    def __init__(
        self,
        openai: OpenAIService,
    ):

        self.openai = openai

    async def extract(
        self,
        text: str,
    ) -> ExtractedFacts:

        response = await self.openai.generate_json(
            prompt=FACT_EXTRACTION_PROMPT,
            response_model=ExtractedFacts,
            user_input=text,
        )

        return ExtractedFacts.model_validate_json(
            response
        )