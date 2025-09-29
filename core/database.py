from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from core.config import configs
from sqlalchemy import Column, DateTime, func

engine = create_engine(configs.DATABASE_URL, pool_pre_ping=True, echo=True, future=True)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

@as_declarative()
class BaseModel:
    id: any
    __name__: str
        
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

def get_db():
    """
    Create a database session.
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
