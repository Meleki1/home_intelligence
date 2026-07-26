import json
import re

from app.domains.AI.schemas.llm import LLMResponseSchema


def _extract_json(response: str) -> dict:
    text = (response or "").strip()
    if not text:
        raise ValueError("Empty LLM response")

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start : end + 1])

    raise ValueError(f"LLM response is not valid JSON: {text[:200]!r}")


def parse_response(response: str | None) -> LLMResponseSchema:
    data = _extract_json(response)

    return LLMResponseSchema(
        intent=data.get("intent", "UNKNOWN"),
        confidence=data.get("confidence", "LOW"),
        signals=data.get("signals", []),
        summary=data.get("summary", ""),
    )
