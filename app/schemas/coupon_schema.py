from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class CouponBase(BaseModel):
    code: str
    type: int
    value: int
    expiry_date: Optional[datetime] = None


class CouponValidateRequest(BaseModel):
    code: str


class CouponValidateResponse(CouponBase):
    model_config = ConfigDict(from_attributes=True)
