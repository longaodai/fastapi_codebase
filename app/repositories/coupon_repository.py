from datetime import datetime

from sqlalchemy.orm import Session

from app.models.coupon import Coupon
from app.repositories.base_repository import BaseRepository


from app.schemas.coupon_schema import CouponValidateRequest

class CouponRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Coupon)

    def get_available(self, data: CouponValidateRequest) -> Coupon:
        return (
            self.db_session.query(Coupon)
            .filter(
                Coupon.code == data.code,
                Coupon.deleted_at.is_(None),
                Coupon.expiry_date >= datetime.now()
            )
            .first()
        )
