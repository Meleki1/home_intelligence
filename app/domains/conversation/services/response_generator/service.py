from app.domains.AI.services.openai import OpenAIService
from .prompt import RESPONSE_GENERATION_PROMPT
from app.domains.planning.schemas import Plan
from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import CognitiveResult
import json

class ResponseGenerationService:

    def __init__(self, openai: OpenAIService):
        self.openai = openai

    async def generate(
        self,
        user_message: str,
        state: ConversationState,
        cognition: CognitiveResult,
        plan: Plan,
    ) -> str:

        context = json.dumps(
            {
                "user_message": user_message,
                "conversation_state": state.model_dump(mode="json"),
                "understanding": cognition.model_dump(mode="json"),
                "plan": plan.model_dump(mode="json"),
            },
            indent=2,
        )

        return await self.openai.generate_text(
            system_prompt=RESPONSE_GENERATION_PROMPT,
            user_prompt=context,
        )