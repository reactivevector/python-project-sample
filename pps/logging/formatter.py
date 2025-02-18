from logging import Formatter


class SimpleFormatter(Formatter):
	def format(self, record):
		return record.msg
