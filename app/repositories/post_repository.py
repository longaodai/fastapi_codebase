from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.models.post import Post
from app.repositories.base_repository import BaseRepository


class PostRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Post)

    def get_list(self, data) -> Post:
        query = self.db_session.query(Post)
        
        if data.get("title"):
            query =  query.filter(Post.title.ilike(f"%{data.get('title')}%"))

        if data.get("per_page"):
            query =  query.limit(data.get("per_page"))
        
        if data.get("with_category"):
            query =  query.options(selectinload(Post.category))

        return  query.all()
