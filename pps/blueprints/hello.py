import logging

from flask import Blueprint

HELLO_BP = Blueprint('hello_world', __name__, url_prefix='/hello')

LOGGER = logging.getLogger(__name__)


@HELLO_BP.route('/')
def hello_world():
	LOGGER.debug('hello_world')
	LOGGER.debug('hello_world')

	return {'message': 'Hello, World! hot reloaded'}
