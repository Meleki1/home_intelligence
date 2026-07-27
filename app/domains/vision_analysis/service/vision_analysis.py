

from app.domains.AI.services.openai import OpenAIService
from app.domains.vision_analysis.prompts.vision_analysis import VISION_PROMPT
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse

import json


class VisionService:
    def __init__(self):
        self.openai = OpenAIService()

    async def analyze(self, image: bytes, mime_type: str) -> VisionAnalysisResponse:

        response = await self.openai.generate_vision(
            prompt=VISION_PROMPT,
            image=image,
            mime_type=mime_type
        )

        
        
        
        data = json.loads(response)

        confidence = data.get("confidence")

        if isinstance(confidence, dict):
            level = confidence.get("level")
            if isinstance(level, str):
                confidence["level"] = level.upper()

        print(json.dumps(data, indent=2))
        return VisionAnalysisResponse.model_validate(data)