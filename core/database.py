from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from core.config import configs

engine = create_engine(configs.DATABASE_URL, pool_pre_ping=True)
print(engine.pool.status())
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

@as_declarative()
class BaseModel:
    id: any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

def get_db():
    print("Creating database session")
    """
    Create a database session.
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        print("Yielding database session")
        yield db
    finally:
        print(engine.pool.status())
        print("Closing database session")
        db.close()
