from .abstract import AbstractCache, BaseCacheConfig
from .exception import CacheException
from .memory_cache import MemoryCacheConfig, create_memory_cache
from .redis import RedisCacheConfig, create_redis_cache

_CACHE_FACTORIES: dict[str, AbstractCache] = {
	RedisCacheConfig: create_redis_cache,
	MemoryCacheConfig: create_memory_cache,
}

_CACHE: AbstractCache = None

CacheConfig = BaseCacheConfig | RedisCacheConfig | MemoryCacheConfig


def setup_cache(options: BaseCacheConfig):
	global _CACHE
	factory_method: callable[AbstractCache] = _CACHE_FACTORIES.get(type(options))
	_CACHE = factory_method(options)


def get_cache() -> AbstractCache:
	if not _CACHE:
		raise CacheException('Cache not initialized')
	return _CACHE
