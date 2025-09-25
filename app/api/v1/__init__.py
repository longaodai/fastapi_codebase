from fastapi import APIRouter

from app.api.v1.coupon import router as coupon_router

v1_routers = APIRouter()
v1_routers.include_router(coupon_router, prefix="/api")
    