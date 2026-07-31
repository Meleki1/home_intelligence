from app.domains.AI.services.openai import OpenAIService
from .prompt import RESPONSE_GENERATION_PROMPT
from app.domains.conversation.models import ConversationState
from app.domains.conversation.services.cognition.schemas import CognitiveResult
from app.domains.planning.schemas import PlanAction, Plan



class ResponseGenerationService:

    def __init__(self, openai: OpenAIService):
        self.openai = openai

    async def generate(
        self,
        user_message: str,
        state: ConversationState,
        cognition: CognitiveResult,
        plan: Plan
    
    ) -> str:

        planner_section = self._build_planner_section(plan)

        user_prompt = f"""
You must follow the planner decision exactly.

==========================
PLANNER DECISION
==========================

{planner_section}

==========================
CURRENT UNDERSTANDING
==========================

Current Knowledge:
{cognition.current_knowledge}

Hypothesis:
{cognition.current_hypothesis}

Summary:
{cognition.summary}

==========================
CONVERSATION STATE
==========================

Affected Area:
{state.affected_area}

Duration:
{state.duration}

Suspected Pest:
{state.suspected_pest}

Image Received:
{state.image_received}

Image Summary:
{state.image_summary}

==========================
LATEST USER MESSAGE
==========================

{user_message}
"""
        print("\n===== RESPONSE PROMPT =====")
        print(user_prompt)
        print("===========================\n")

        return await self.openai.generate_text(
            system_prompt=RESPONSE_GENERATION_PROMPT,
            user_prompt=user_prompt,
        )

    def _build_planner_section(self, plan: Plan) -> str:

        section = f"""
Next Action:
{plan.next_action.value}

Priority:
{plan.priority.value}
"""

        if plan.next_action == PlanAction.ASK_FOLLOW_UP:

            section += f"""

Missing Information:
{", ".join(plan.missing_information)}

Follow-up Questions:
{chr(10).join(f"- {q}" for q in plan.follow_up_questions)}
"""

        elif plan.next_action == PlanAction.PROVIDE_GUIDANCE:

            section += f"""

Explanation:
{plan.explanation}

Recommended Actions:
{chr(10).join(f"- {a}" for a in plan.recommended_actions)}
"""

            if plan.safety_warnings:
                section += f"""

Safety Warnings:
{chr(10).join(f"- {w}" for w in plan.safety_warnings)}
"""

        elif plan.next_action == PlanAction.RECOMMEND_BOOKING:

            section += f"""

Explanation:
{plan.explanation}

Booking Reason:
{plan.booking_reason}
"""

        elif plan.next_action == PlanAction.EMERGENCY:

            section += f"""

Explanation:
{plan.explanation}

Safety Warnings:
{chr(10).join(f"- {w}" for w in plan.safety_warnings)}
"""
        elif plan.next_action == PlanAction.OUT_OF_SCOPE:

            section += f"""

Explanation:
{plan.explanation}
"""

        return section