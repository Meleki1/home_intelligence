from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import UploadFile
from pydantic import ValidationError
from app.interfaces.api.telegram.schemas import ImageInput


from app.domains.chat.schemas.chat import (
    ChatRequest,
    ResponseSchema,
)
from app.domains.chat.services.chat import ChatService


router = APIRouter()

chat_service = ChatService()


@router.post(
    "/",
    response_model=ResponseSchema,
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": ChatRequest.model_json_schema(),
                },
                "multipart/form-data": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "message": {"type": "string"},
                            "conversation_id": {"type": "string"},
                            "home_id": {"type": "string"},
                            "image": {
                                "type": "string",
                                "format": "binary",
                            },
                        },
                        "required": ["message"],
                    }
                },
            }
        }
    },
)
async def chat(request: Request) -> ResponseSchema:
    content_type = request.headers.get("content-type", "")


    if content_type.startswith("application/json"):
        payload = await request.json()

        try:
            chat_request = ChatRequest.model_validate(payload)
        except ValidationError as e:
            raise HTTPException(
                status_code=422,
                detail=e.errors(),
            )

        return await chat_service.chat(
            request=chat_request,
            image=None,
        )

    if "multipart/form-data" in content_type:
        form = await request.form()
        message = form.get("message")
        if not message:
            raise HTTPException(
                status_code=422,
                detail="message is required",
            )

        chat_request = ChatRequest(
            message=str(message),
            conversation_id=form.get("conversation_id") or None,
            home_id=form.get("home_id") or None,
        )

        image_field = form.get("image")

        image = None

        if image_field and getattr(image_field, "filename", None):
            image = ImageInput(
                data=await image_field.read(),
                mime_type=image_field.content_type,
                filename=image_field.filename,
                source="web",
            )

        return await chat_service.chat(
            request=chat_request,
            image=image,
        )

       

    raise HTTPException(
        status_code=415,
        detail=(
            "Unsupported content type. Use application/json for text-only "
            "requests or multipart/form-data for text with an optional image."
        ),
    )
