from fastapi import APIRouter, Depends
from typing import Optional

from core.dependence import get_post_service
from core.response import ResponseSuccess, ResponseError

from app.services.post_service import PostService
from app.schemas.post_schema import PostResponse, PostCreate

from app.enums.error_code_enum import ErrorCodeEnum

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

@router.get(
    "/",
    response_model=ResponseSuccess,
)
async def get(title: Optional[str] = None, per_page: Optional[int] = 10, service: PostService = Depends(get_post_service)):
    posts = service.get_list({
        "title": title,
        "per_page": per_page,
        "with_category": True,
    })

    return ResponseSuccess(
        data=[PostResponse.model_validate(post) for post in posts]
    )

@router.post(
    "/",
    response_model=ResponseSuccess,
)
async def create(data: PostCreate, service: PostService = Depends(get_post_service)):
    try:
        post = service.add(data)

        if not post:
            return ResponseError(
                error_code=ErrorCodeEnum.CREATE_ERROR.value,
                message="Create post failed",
            ).dict()

        return ResponseSuccess(
            data=PostResponse.model_validate(post)
        )
    except Exception as e:
        return ResponseError(
            error_code=ErrorCodeEnum.CREATE_ERROR.value,
            message=str(e),
        ).dict()
