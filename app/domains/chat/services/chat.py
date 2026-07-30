from uuid import UUID
from app.domains.chat.schemas.chat import ChatRequest, ResponseSchema
from app.domains.understanding.schemas.understanding import UnderstandingSchema
from app.interfaces.api.telegram.schemas import ImageInput
from app.core.container import ServiceContainer

class ChatService:

    def __init__(self):

        container = ServiceContainer()

        self.vision_service = container.vision_service
        self.understanding_service = (
            container.understanding_service
        )
        self.response_generator = (
            container.response_generator
        )

    async def chat(
        self,
        request: ChatRequest,
        image: ImageInput | None = None,
    ) -> ResponseSchema:

        image_analysis = None

        if image is not None:

            image_analysis = (
                await self.vision_service.analyze(
                    image=image.data,
                    mime_type=image.mime_type,
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

        reply = (
            await self.response_generator.generate(
                user_message=request.message,
                state=understanding.state,
                cognition=understanding.cognition,
                plan=understanding.plan
            )
        )

        return ResponseSchema(
            message=reply,
            intent=understanding.plan.next_action.value,
            confidence=understanding.cognition.confidence,
            next_best_step=understanding.cognition.next_best_step,
            conversation_id=request.conversation_id,
        )