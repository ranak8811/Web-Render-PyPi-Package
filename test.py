from WebRender.logger import logger
from WebRender.custom_execution import InvalidURLException

# logger.info("Hello World")

try:
    raise InvalidURLException('Provided URL is invalid')
except Exception as e:
    logger.error(f'Caught Exception: {e}')