from app.models.coupon import Coupon

from app.services.base_service import BaseService

from app.repositories.coupon_repository import CouponRepository


from app.schemas.coupon_schema import CouponValidateRequest

class CouponService(BaseService):
    def __init__(self, repo: CouponRepository):
        super().__init__(repo)

    def get_available(self, data: CouponValidateRequest) -> Coupon:
        return self._repository.get_available(data)