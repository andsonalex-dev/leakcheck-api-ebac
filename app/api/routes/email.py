from fastapi import APIRouter

from app.services.leakcheck_service import LeakCheckService

router = APIRouter()

service = LeakCheckService()


@router.get("/{email}")
async def search_email(email: str):

    return await service.search_email(email)