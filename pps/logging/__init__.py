import logging
import logging.config

from pps.file.file import load_yaml_file

from .config import LoggingConfig


def setup_logging(options: LoggingConfig):
	logging.config.dictConfig(load_yaml_file(options.config_file_path))
