from fastapi import APIRouter, Depends, HTTPException

from core.dependence import get_coupon_service
from core.response import ResponseSuccess, ResponseError

from app.services.coupon_service import CouponService
from app.schemas.coupon_schema import CouponValidateRequest, CouponValidateResponse
from app.enums.error_code_enum import ErrorCodeEnum

router = APIRouter(
    prefix="/coupons",
    tags=["coupons"],
)

@router.post(
    "/validate",
    response_model=ResponseSuccess,
)
async def validate(request: CouponValidateRequest, service: CouponService = Depends(get_coupon_service)):
    coupon = service.get_available(request)

    if not coupon:
        raise HTTPException(
            status_code=404,
            detail=ResponseError(
                message="Coupon not found",
                error_code=ErrorCodeEnum.COUPON_NOT_FOUND.value
            ).model_dump(),
        )
    
    return ResponseSuccess(
        data=CouponValidateResponse.model_validate(coupon)
    )
