from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.coupon_service import CouponService
from app.repositories.coupon_repository import CouponRepository


def get_coupon_service(db: Session = Depends(get_db)) -> CouponService:
    repo = CouponRepository(db)
    return CouponService(repo)

