from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, func
from app.core.database import BaseModel


class Coupon(BaseModel):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True, index=True, nullable=False)
    type = Column(SmallInteger, nullable=False)
    value = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
