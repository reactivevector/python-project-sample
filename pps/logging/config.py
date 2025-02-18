from pydantic import BaseModel


class LoggingConfig(BaseModel):
	config_file_path: str = 'logging.yaml'
