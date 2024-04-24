from fastapi import APIRouter, status
from core.settings import settings
from core.utils.responses import EnvelopeResponse

router = APIRouter(tags=["Health Check"])


@router.get(
    "/health", status_code=status.HTTP_200_OK, summary="Health service", response_model=EnvelopeResponse
)
def health_check() -> EnvelopeResponse:
    result = {
        'status' : 'ok'
    }
    return EnvelopeResponse(success=True, data=result)
