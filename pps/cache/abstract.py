from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field


class BaseCacheConfig(BaseModel):
	type: str = Field(..., description='Cach type, eg: redis, memory')
	max_size: int = 1024


class AbstractCache(ABC):
	def __init__(self, options: BaseCacheConfig) -> None:
		self.options = options

	@abstractmethod
	def set(self, key: str, value: Any) -> None:
		pass

	@abstractmethod
	def get(self, key: str) -> Any:
		pass

	@abstractmethod
	def delete(self, key: str) -> None:
		pass

	@abstractmethod
	def keys(self, pattern: str) -> list[str]:
		pass

	@abstractmethod
	def flushdb(self) -> None:
		pass
