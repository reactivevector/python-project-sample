from typing import Literal

import redis

from pps.cache.abstract import AbstractCache, BaseCacheConfig


class RedisCacheConfig(BaseCacheConfig):
	type: Literal['redis'] = 'redis'
	host: str = 'localhost'
	port: int = 6379
	db: int = 0


class RedisCache(AbstractCache):
	def __init__(self, options: RedisCacheConfig, redis_instance: redis.StrictRedis):
		super().__init__(options)
		self.redis = redis_instance

	def set(self, key, value):
		self.redis.set(key, value)

	def get(self, key):
		return self.redis.get(key)

	def delete(self, key):
		self.redis.delete(key)

	def keys(self, pattern):
		return self.redis.keys(pattern)

	def flushdb(self):
		self.redis.flushdb()


def create_redis_cache(options: RedisCacheConfig = None) -> RedisCache:
	return RedisCache(
		options, redis.StrictRedis(host=options.host, port=options.port, db=options.db)
	)
