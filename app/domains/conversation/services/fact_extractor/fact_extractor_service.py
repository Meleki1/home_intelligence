from app.domains.conversation.services.fact_extractor.prompt import FACT_EXTRACTION_PROMPT
from app.domains.conversation.services.fact_extractor.schema import ExtractedFacts
from app.domains.AI.services.openai import OpenAIService
import logging

logger = logger = logging.getLogger(__name__)

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

        result = await self.openai.generate_json(
            system_prompt=FACT_EXTRACTION_PROMPT,
            user_prompt=text,
            response_model=ExtractedFacts,
        )
        logger.info("Extracted facts: %s", result.model_dump())
        return result