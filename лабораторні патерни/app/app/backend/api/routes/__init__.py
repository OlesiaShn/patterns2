# backend/api/routes/__init__.py
from fastapi import APIRouter
from backend.api.routes.weather.current import (
    translation_router,
    detection_router,
    language_router
)

router = APIRouter()

router.include_router(
    translation_router,
    prefix="/api",
    tags=["translation"],
    include_in_schema=True
)

router.include_router(
    detection_router,
    prefix="/api",
    tags=["language_detection"],
    include_in_schema=True
)

router.include_router(
    language_router,
    prefix="/api",
    tags=["supported_languages"],
    include_in_schema=True
)