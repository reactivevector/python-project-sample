from .exception import DbException
from .mongodb import MongoDbClient, MongoDbConfig, create_mongo_db

_DATABASE: MongoDbClient = None


def setup_database(options: MongoDbConfig):
	global _DATABASE
	_DATABASE = create_mongo_db(options)


def get_database_client() -> MongoDbClient:
	if not _DATABASE:
		raise DbException('Database not initialized')
	return _DATABASE
