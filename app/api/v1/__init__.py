from fastapi import APIRouter

from app.api.v1.coupon import router as coupon_router
from app.api.v1.post import router as post_router

v1_routers = APIRouter()
v1_routers.include_router(coupon_router, prefix="/api")
v1_routers.include_router(post_router, prefix="/api")
    