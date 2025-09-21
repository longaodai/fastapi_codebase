import redis.asyncio as aioredis
from app.core.config import configs

class RedisClient:
    def __init__(self):
        self._redis = None

    async def init_redis(self):
        if self._redis is None:
            self._redis = aioredis.from_url(
                configs.REDIS_URL,
                encoding="utf-8",
                decode_responses=True,
            )
        return self._redis

    async def get_client(self):
        if self._redis is None:
            await self.init_redis()
        return self._redis


redis_client = RedisClient()
