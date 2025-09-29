from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from core.database import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    posts = relationship("Post", back_populates="category")