from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def health():
    """
    Basic health check
    """

    return {
        "status": "healthy",
        "service": "Home-intelligence-platform",
        "version": "1.0.0"
    }