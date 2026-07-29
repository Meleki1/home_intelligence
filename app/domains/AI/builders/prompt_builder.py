import json

from app.domains.AI.prompts.system import(
    SYSTEM_PROMPT
)

from app.domains.AI.prompts.understanding import(
    UNDERSTANDING_PROMPT
)

from app.domains.AI.products.pest_control.prompt import(
    PEST_CONTROL_PROMPT
)

from app.domains.understanding.schemas.understanding import UnderstandingResult

PEST_KEYWORDS=[

    "rat",

    "ants",

    "termites",

    "cockroach",

    "rodent",

    "mosquito",

    "flies",

    "insects"

]


def build_prompt(understanding: UnderstandingResult | dict):

    if isinstance(understanding, UnderstandingResult):
        user_input = understanding.user_input
        image_analysis = understanding.image_analysis
    else:
        user_input = understanding["user_input"]
        image_analysis = understanding.get("image_analysis")

    prompts = [
        SYSTEM_PROMPT,
        UNDERSTANDING_PROMPT,
    ]

    message = user_input.lower()
    if image_analysis is not None:
        prompts.append(PEST_CONTROL_PROMPT)
        analysis_payload = (
            image_analysis.model_dump()
            if hasattr(image_analysis, "model_dump")
            else image_analysis
        )
        prompts.append(
            f"""
        IMAGE ANALYSIS:
        {json.dumps(analysis_payload, indent=2)}
        """
        )

    elif any(
        keyword in message
        for keyword in PEST_KEYWORDS
    ):
        prompts.append(PEST_CONTROL_PROMPT)

    prompts.append(
        f"""
        USER MESSAGE:
        {user_input}
        """
    )

    return "\n".join(prompts)