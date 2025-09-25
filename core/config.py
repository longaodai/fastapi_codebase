import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Configs(BaseSettings):
    # Base
    ENV: str = os.getenv("ENV", "development")
    API: str = "/api"
    PROJECT_NAME: str = "FAST-API"

    # Date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")


configs = Configs()
