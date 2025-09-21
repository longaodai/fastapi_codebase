from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException

from app.core.config import configs
from app.core.redis import redis_client
from app.core.exception import validation_exception_handler, http_exception_handler, global_exception_handler
from app.api.v1.routes import routers as v1_routers


class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            docs_url="/docs",
            version="0.0.1",
        )


        @self.app.get("/health")
        def health_check():
            return {"status": "healthy"}

        self.app.include_router(v1_routers)


app_creator = AppCreator()
app = app_creator.app

app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
async def startup_event():
    await redis_client.init_redis()

@app.on_event("shutdown")
async def shutdown_event():
    client = await redis_client.get_client()
    await client.close()
