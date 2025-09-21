from fastapi import APIRouter

from app.api.v1.endpoints.coupon import router as coupon_router

routers = APIRouter()

routers.include_router(coupon_router, prefix="/api")
    