from fastapi import APIRouter
from src.rest.api.hotel import router as hotel_router

router = APIRouter()

router.include_router(hotel_router, prefix='/v1')
