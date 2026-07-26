#prompt_builder.py

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


def build_prompt(understanding: dict):

    prompts = [
        SYSTEM_PROMPT,
        UNDERSTANDING_PROMPT,
    ]

    user_input = understanding["user_input"]
    message = user_input.lower()

    image_analysis = understanding.get("image_analysis")
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