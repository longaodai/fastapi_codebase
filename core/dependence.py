from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db

from app.services.coupon_service import CouponService
from app.repositories.coupon_repository import CouponRepository

from app.services.post_service import PostService
from app.repositories.post_repository import PostRepository
from app.repositories.category_repository import CategoryRepository


def get_coupon_service(db: Session = Depends(get_db)) -> CouponService:
    repo = CouponRepository(db)
    return CouponService(repo)

def get_post_service(db: Session = Depends(get_db)) -> PostService:
    repo = PostRepository(db)
    category_repo = CategoryRepository(db)
    return PostService(repo, category_repo)

