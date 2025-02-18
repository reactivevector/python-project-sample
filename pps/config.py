from pydantic import BaseModel

from pps.cache import CacheConfig, setup_cache
from pps.database.mongodb import setup_database
from pps.database.mongodb.mongodb import MongoDbConfig
from pps.logging import setup_logging
from pps.logging.config import LoggingConfig


class AppConfig(BaseModel):
	mongodb: MongoDbConfig

	cache: CacheConfig

	logging: LoggingConfig

	tmp_dir_path: str


def setup_app_config(config: AppConfig):
	setup_cache(config.cache)
	setup_database(config.mongodb)
	setup_logging(config.logging)
