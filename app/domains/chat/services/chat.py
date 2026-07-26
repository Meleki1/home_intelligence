from uuid import UUID

from fastapi import UploadFile

from app.domains.AI.services.llm import LLMService
from app.domains.chat.builders.response_builder import (
    build_response,
    resolve_next_best_step,
    SIMPLE_INTENTS,
)
from app.domains.chat.schemas.chat import (
    ChatRequest,
    ResponseSchema,
)
from app.domains.understanding.schemas.understanding import (
    UnderstandingSchema,
)
from app.domains.understanding.services.understanding import (
    UnderstandingService,
)
from app.domains.vision_analysis.service.vision_analysis import VisionService
from app.interfaces.api.telegram.schemas import ImageInput

class ChatService:

    def __init__(self):

        self.llm_service = LLMService()

        self.understanding_service = (
            UnderstandingService()
        )

        self.vision_service = VisionService()

    async def chat(
        self,
        request: ChatRequest,
        image: ImageInput | None = None,
    ) -> ResponseSchema:

        image_analysis = None

        if image is not None:

            image_bytes = await image.read()

            image_analysis = (
                await self.vision_service.analyze(
                    image=image_bytes,
                    mime_type=image.content_type,
                )
            )



        understanding = (
            await self.understanding_service.understand(
                UnderstandingSchema(
                    user_input=request.message,
                    image_analysis=image_analysis,
                    home_id=(
                        UUID(request.home_id)
                        if request.home_id
                        else None
                    ),
                    conversation_id=request.conversation_id,
                )
            )
        )

        llm_response = await self.llm_service.generate(
            understanding
        )

        message = build_response(
            llm_response,
            understanding,
        )

        next_best_step = (
            None
            if llm_response.intent in SIMPLE_INTENTS
            else resolve_next_best_step(
                understanding
            )
        )

        return ResponseSchema(
            message=message,
            intent=llm_response.intent,
            confidence=llm_response.confidence,
            next_best_step=next_best_step,
            conversation_id=request.conversation_id,
        )