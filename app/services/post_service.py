from app.models.post import Post

from app.services.base_service import BaseService

from app.repositories.post_repository import PostRepository
from app.repositories.category_repository import CategoryRepository

from app.schemas.post_schema import PostCreate

class PostService(BaseService):
    def __init__(self, repo: PostRepository, category_repo: CategoryRepository):
        super().__init__(repo)
        self._category_repo = category_repo

    def get_list(self, data) -> list[Post]:
        return self._repository.get_list(data)
    
    def add(self, data: PostCreate) -> Post | None:
        category = self._category_repo.read_by_id(data.category_id)
        if not category:
            raise ValueError(f"Category id={data.category_id} not found")
        
        return super().add(data)