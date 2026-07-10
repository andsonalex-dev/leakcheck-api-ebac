from fastapi import APIRouter

from app.api.routes import email
from app.api.routes import name
from app.api.routes import health

router = APIRouter()

router.include_router(
    email.router,
    prefix="/api/v1/email",
    tags=["Email"]
)

router.include_router(
    name.router,
    prefix="/api/v1/username",
    tags=["Username"]
)

router.include_router(
    health.router,
    tags=["Health"]
)