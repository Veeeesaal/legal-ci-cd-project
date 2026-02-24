from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "message": "Legal App Running Successfully",
        "status": "healthy"
    }