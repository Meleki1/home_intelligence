import json
from app.domains.planning.schemas import Plan
from app.domains.AI.services.openai import OpenAIService
from app.domains.conversation.services.state_service import ConversationState
from app.domains.conversation.models import CognitiveResult
from .prompt import PLANNER_PROMPT
from app.domains.planning.exceptions import PlanningValidationError


class PlannerService:
    def __init__(self, openai: OpenAIService):
        print("PlannerService __init__ called")
        print("OpenAI:", openai)
        self.openai = openai


    async def plan(
        self,
        state: ConversationState,
        cognition: CognitiveResult,
    ) -> Plan:


        context = {
            "conversation_state": state.model_dump(mode="json"),
            "understanding": cognition.model_dump(mode="json"),
        }
        print(Plan)
        for attempt in range(2):

            try:

                plan = await self.openai.generate_json(
                    system_prompt=PLANNER_PROMPT,
                    user_prompt=json.dumps(
                        context,
                        indent=2,
                    ),
                    response_model=Plan,
                )


                return plan

            except PlanningValidationError:

                if attempt == 1:
                    raise

