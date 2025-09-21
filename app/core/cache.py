import json
from typing import Any, Optional

from app.core.redis import redis_client


class RedisCache:
    def __init__(self):
        print("RedisCache initialized")
        self._redis = None

    async def get_client(self):
        if self._redis is None:
            self._redis = await redis_client.get_client()
        return self._redis

    # ---------- Core methods ----------
    async def set(self, key: str, value: Any, expire: int = 3600):
        client = await self.get_client()
        # serialize object to json
        if not isinstance(value, str):
            value = json.dumps(value)
        await client.set(key, value, ex=expire)

    async def get(self, key: str) -> Optional[Any]:
        client = await self.get_client()
        value = await client.get(key)
        if value is None:
            return None
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    async def delete(self, key: str):
        client = await self.get_client()
        await client.delete(key)

    async def exists(self, key: str) -> bool:
        client = await self.get_client()
        return await client.exists(key) > 0

    async def close(self):
        if self._redis:
            await self._redis.close()


cache = RedisCache()
