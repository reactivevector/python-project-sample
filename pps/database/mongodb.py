import logging
from contextlib import contextmanager
from typing import Any

from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.results import (
	DeleteResult,
	InsertManyResult,
	InsertOneResult,
	UpdateResult,
)

LOGGER = logging.getLogger(__name__)


class MongoDbConfig(BaseModel):
	host: str = 'localhost'
	port: int = 27017
	db: str = 'pps'


class MongoDbCollection:
	def __init__(self, collection: Collection):
		self.collection = collection

	def insert(self, document: dict, session: ClientSession = None) -> InsertOneResult:
		return self.collection.insert_one(document, session=session)

	def insert_many(self, documents: list[dict]) -> InsertManyResult:
		return self.collection.insert_many(documents)

	def find_one(self, filters: dict) -> Any | None:
		return self.collection.find_one(filters)

	def find_all(self, filters: dict) -> list[dict]:
		return list(self.collection.find(filters))

	def update_one(
		self, filters: dict, updates: dict, session: ClientSession = None
	) -> UpdateResult:
		return self.collection.update_one(filters, updates, session=session)

	def update_many(
		self, filters: dict, updates: dict, session: ClientSession = None
	) -> UpdateResult:
		return self.collection.update_many(filters, updates, session=session)

	def delete_one(self, filters: dict, session: ClientSession = None) -> DeleteResult:
		return self.collection.delete_one(filters, session=session)

	def delete_many(self, filters: dict, session: ClientSession = None) -> DeleteResult:
		return self.collection.delete_many(filters, session=session)


class MongoDbClient:
	def __init__(self, options: MongoDbConfig, mongo_client: MongoClient):
		self.options = options
		self.mongo_client = mongo_client
		self.db = self.mongo_client[self.options.db]

	@contextmanager
	def open_session(self):
		session = self.mongo_client.start_session()
		LOGGER.debug(f'open_session: {session.session_id}')
		try:
			yield session
		finally:
			session.end_session()
		LOGGER.debug(f'end_session: {session.session_id}')

	def get_collection(self, name: str):
		return MongoDbCollection(self.db.get_collection(name))


def create_mongo_db(options: MongoDbConfig = None) -> MongoDbClient:
	mongo_instance = MongoClient(options.host, options.port)
	return MongoDbClient(options, mongo_instance)
