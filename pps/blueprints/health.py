from flask import Blueprint

HEALTH_BP = Blueprint('health', __name__, url_prefix='/health')


@HEALTH_BP.route('/')
def health():
	return {'status': 'ok'}
