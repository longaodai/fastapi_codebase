from typing import Any, TypeVar, Optional
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")

class BaseRepository():
    def __init__(self, db_session: Session, model: ModelType) -> None:
        self.db_session = db_session
        self.model = model

    def create(self, schema: Any) -> ModelType:
        obj = self.model(**schema.dict())
        self.db_session.add(obj)
        self.db_session.commit()
        self.db_session.refresh(obj)
        return obj

    def read_by_id(self, id: int) -> Optional[ModelType]:
        return self.db_session.query(self.model).filter(self.model.id == id).first()

    def update(self, id: int, schema: Any) -> Optional[ModelType]:
        obj = self.read_by_id(id)
        if not obj:
            return None
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        self.db_session.commit()
        self.db_session.refresh(obj)
        return obj
