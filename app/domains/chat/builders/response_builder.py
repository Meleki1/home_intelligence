import random
from typing import Any

from app.domains.AI.schemas.llm import LLMResponseSchema
from app.domains.chat.enums.enum import Intent, NextBestStep
from app.domains.decision.schemas.decision import DecisionSchema
from app.domains.recommendations.schemas.recommendation import RecommendationSchema
from app.domains.understanding.schemas.understanding import UnderstandingResult

GREETING_RESPONSES = [
    "Hello! I'm HOME AI OS. How can I help you today?",
    "Hello! It's nice hearing from you. How can I assist you today?",
    "Welcome! I'm HOME AI OS. What would you like help with today?",
]

APPRECIATION_RESPONSES = [
    "You're welcome! I'm always happy to help.",
    "I'm glad I could help. Please let me know if there's anything else I can do for you.",
]

DEFAULT_RESPONSE = (
    "I'm here to help with anything related to your home. "
    "Could you tell me a bit more about what you need?"
)

SIMPLE_INTENTS = {
    Intent.GREETING.value,
    Intent.APPRECIATION.value,
}

ISSUE_INTENTS = {
    Intent.HOME_ISSUE.value,
    Intent.QUESTION.value,
    Intent.GENERAL_HELP.value,
    Intent.PRICE_REQUEST.value,
    Intent.CONTINUE_CONVERSATION.value,
    Intent.UNKNOWN.value,
}


def _as_dict(
    understanding: UnderstandingResult | dict[str, Any] | None,
) -> dict[str, Any] | None:
    if understanding is None:
        return None
    if isinstance(understanding, UnderstandingResult):
        return {
            "user_input": understanding.user_input,
            "image_analysis": understanding.image_analysis,
            "decision": understanding.decision,
            "recommendations": understanding.recommendations,
            "next_best_step": [understanding.cognition.next_best_step],
            "unknown_context": [],
            "summary": understanding.cognition.summary,
        }
    return understanding


def build_response(
    llm_response: LLMResponseSchema,
    understanding: UnderstandingResult | dict[str, Any] | None = None,
) -> str:
    intent = llm_response.intent

    if intent == Intent.GREETING.value:
        return random.choice(GREETING_RESPONSES)

    if intent == Intent.APPRECIATION.value:
        return random.choice(APPRECIATION_RESPONSES)

    parts: list[str] = []

    if llm_response.summary:
        parts.append(llm_response.summary)

    understanding_data = _as_dict(understanding)
    if understanding_data:
        image_analysis = understanding_data.get("image_analysis")
        if image_analysis:
            parts.append(image_analysis.summary)

        recommendation = understanding_data.get("recommendations")
        if isinstance(recommendation, RecommendationSchema):
            parts.append(recommendation.description)

        next_steps = understanding_data.get("next_best_step") or []
        if next_steps:
            parts.append(next_steps[0])

        if intent in ISSUE_INTENTS:
            unknown_context = understanding_data.get("unknown_context") or []
            if unknown_context:
                questions = "\n".join(
                    f"- {question.strip().capitalize()}"
                    for question in unknown_context[:2]
                )
                parts.append(f"To help further:\n{questions}")

    if parts:
        return "\n\n".join(parts)

    return DEFAULT_RESPONSE


def resolve_next_best_step(
    understanding: UnderstandingResult | dict[str, Any] | None,
) -> str | None:
    understanding_data = _as_dict(understanding)
    if not understanding_data:
        return None

    next_steps = understanding_data.get("next_best_step") or []
    if next_steps:
        next_step = next_steps[0].lower()
        if "picture" in next_step or "image" in next_step or "upload" in next_step:
            return NextBestStep.UPLOAD_IMAGE.value
        if "information" in next_step or "provide" in next_step:
            return NextBestStep.ASK_MORE_QUESTIONS.value

    decision = understanding_data.get("decision")
    if isinstance(decision, DecisionSchema):
        if decision.next_action in {"ANALYZE_IMAGE", "REQUEST_IMAGE"}:
            return NextBestStep.UPLOAD_IMAGE.value
        if decision.next_action in {"CONTINUE_CONVERSATION", "ASK_FOLLOW_UP"}:
            return NextBestStep.ASK_MORE_QUESTIONS.value

    return NextBestStep.CONTINUE_CONVERSATION.value
