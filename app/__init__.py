from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException

from core.config import configs
from core.redis import redis_client
from core.exception import validation_exception_handler, http_exception_handler, global_exception_handler

from app.api.v1 import v1_routers


class AppCreator:
    def __init__(self):
        self.app = FastAPI(title=configs.PROJECT_NAME)
        self._register_routes()
        self._register_events()
        self._register_exception_handlers()


    def _register_routes(self):
        @self.app.get("/health")
        def health_check():
            return {"status": "healthy"}

        self.app.include_router(v1_routers)


    def _register_events(self):
        @self.app.on_event("startup")
        async def startup_event():
            await redis_client.init_redis()

        @self.app.on_event("shutdown")
        async def shutdown_event():
            client = await redis_client.get_client()
            await client.close()
    
    def _register_exception_handlers(self):
        self.app.add_exception_handler(Exception, global_exception_handler)
        self.app.add_exception_handler(HTTPException, http_exception_handler)
        self.app.add_exception_handler(RequestValidationError, validation_exception_handler)

    def get_app(self):
        return self.app

