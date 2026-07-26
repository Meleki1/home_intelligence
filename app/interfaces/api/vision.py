from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import status

from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse
from app.domains.vision_analysis.service.vision_analysis import VisionService

router = APIRouter(
    prefix="/vision",
    tags=["Vision"],
)

vision_service = VisionService()


@router.post(
    "",
    response_model=VisionAnalysisResponse,
    status_code=status.HTTP_200_OK,
)
async def analyze_image(image: UploadFile = File(...),) -> VisionAnalysisResponse:

    try: 
        MAX_IMAGE_SIZE = 10 * 1024 * 1024
        ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
        
        
        if image.content_type not in ALLOWED_IMAGE_TYPES:
            raise HTTPException(
            status_code=400,
            detail="Unsupported image format.",
        )

        image_bytes = await image.read()

        if len(image_bytes) > MAX_IMAGE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="Image exceeds the 10 MB limit.",
            )

        return await vision_service.analyze(
            image=image_bytes,
            mime_type=image.content_type,
        )
    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to analyze image at this time."
        )