from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, func
from core.database import BaseModel


class Coupon(BaseModel):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, unique=True, index=True, nullable=False)
    type = Column(SmallInteger, nullable=False)
    value = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=True)
