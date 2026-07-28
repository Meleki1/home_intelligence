from app.domains.conversation.services.fact_extractor.prompt import FACT_EXTRACTION_PROMPT
from app.domains.conversation.services.fact_extractor.schema import ExtractedFacts

class FactExtractionService:

    def __init__(self, openai):

        self.openai = openai

    async def extract(
        self,
        text: str,
    ) -> ExtractedFacts:

        response = await self.openai.generate_json(
            prompt=FACT_EXTRACTION_PROMPT,
            user_input=text,
        )

        return ExtractedFacts.model_validate_json(
            response
        )