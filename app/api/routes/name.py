from fastapi import APIRouter

from app.services.leakcheck_service import LeakCheckService

router = APIRouter()

service = LeakCheckService()


@router.get("/{username}")
async def search_username(username: str):

    return await service.search_username(username)