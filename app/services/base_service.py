from typing import Any, Protocol, Optional, List, TypeVar, Generic

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")


class RepositoryProtocol:
    def create(self, schema: SchemaType) -> ModelType: ...
    def read_by_id(self, id: int) -> Optional[ModelType]: ...
    def update(self, id: int, schema: SchemaType) -> Optional[ModelType]: ...

class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    def get_by_id(self, id: int) -> Any:
        return self._repository.read_by_id(id)

    def add(self, schema: Any) -> Any:
        return self._repository.create(schema)

    def update(self, id: int, schema: Any) -> Any:
        return self._repository.update(id, schema)
