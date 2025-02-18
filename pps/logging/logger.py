from logging import Logger


class PpsLogger(Logger):
	def __init__(self, name):
		super().__init__(name)
		self.name = name
