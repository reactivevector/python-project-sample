from flask import Blueprint, redirect, render_template, url_for

from pps.database.collections import message

MESSAGE_BP = Blueprint('message', __name__, url_prefix='/message')


@MESSAGE_BP.route('/')
def index():
	messages = message.find_messages()
	return render_template('message/index.html', messages=messages)


@MESSAGE_BP.route('/messages', methods=['POST'])
def create_message():
	# message = Message(id=int(time.time() * 1000)
	# , text=request.form.get('message_text'))
	# collection = get_database_client().get_collection('messages')
	# collection.insert(message.model_dump())
	return redirect(url_for('message.index'))


@MESSAGE_BP.route('/messages/<int:message_id>', methods=['POST'])
def delete_message(message_id):
	# collection = get_database_client().get_collection('messages')
	# collection.delete_one({'id': message_id})
	return redirect(url_for('message.index'))
