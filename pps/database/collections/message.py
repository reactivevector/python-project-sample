import logging
from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel

from pps.database import get_database_client

LOGGER = logging.getLogger(__name__)


class Message(BaseModel):
	id: int
	text: str
	created_at: datetime = datetime.now()


def find_messages() -> list[Message]:
	try:
		db_client = get_database_client()
		collection = db_client.get_collection('messages')
		messages = [Message(**message) for message in collection.find_all({})]
	except Exception as e:
		LOGGER.error(f'Error finding messages: {e}')
		messages = []

	return messages


def update_message(filters: dict, message: dict) -> Message:
	try:
		db_client = get_database_client()
		collection = db_client.get_collection('messages')
		updates = {'$set': message}
		update_result = collection.update_one(filters, updates)
		updated_message = Message(
			collection.find_one({'_id': ObjectId(update_result.upserted_id)})
		)
	except Exception as e:
		LOGGER.error(f'Error update message: {e}')

	return updated_message
