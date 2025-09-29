from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional
from app.schemas.category_schema import CategoryResponse


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None


class PostCreate(PostBase):
    category_id: int
    title: str = Field(..., max_length=255)
    content: str | None = Field(None, max_length=2000)


class PostResponse(PostBase):
    id: int
    created_at: datetime
    category: Optional[CategoryResponse] = None

    model_config = ConfigDict(from_attributes=True)
