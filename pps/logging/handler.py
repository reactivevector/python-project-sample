from logging import Handler


class ConsoleHandler(Handler):
	def __init__(self):
		super().__init__()

	def emit(self, record):
		print(record.msg)
		self.flush()
