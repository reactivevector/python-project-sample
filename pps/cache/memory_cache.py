import fnmatch
from collections import OrderedDict
from typing import Any, Literal

from pps.cache.abstract import AbstractCache, BaseCacheConfig


class MemoryCacheConfig(BaseCacheConfig):
	type: Literal['memory'] = 'memory'


class MemoryCache(AbstractCache):
	def __init__(self, options: MemoryCacheConfig):
		super().__init__(options)
		self.cache: OrderedDict[str, Any] = OrderedDict()

	def get(self, key: str) -> Any:
		return self.cache.get(key)

	def set(self, key: str, value: bytes):
		self.cache[key] = value
		if len(self.cache) > self.options.max_size:
			self.cache.pop(next(iter(self.cache)))

	def delete(self, key: str):
		self.cache.pop(key, None)

	def keys(self, pattern: str):
		return [key for key in self.cache if fnmatch.fnmatch(key, pattern)]

	def flushdb(self):
		self.cache.clear()


def create_memory_cache(options: MemoryCacheConfig = None) -> MemoryCache:
	return MemoryCache(options)
