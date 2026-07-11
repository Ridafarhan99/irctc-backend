import sys
# from src.config.logger import logger
from loguru import logger
from src.config.settings import settings

# 1. Clear default handlers to avoid duplicate log outputs
logger.remove()

# 2. Replaces: winston.format.printf(...)
# We define the exact same text structure using Loguru's format tokens
log_format = "[{time:YYYY-MM-DDTHH:mm:ss.SSSZ}] [{level}] [{extra[service]}]: {message}"

# 3. Replaces: transports: [new winston.transports.Console()] & level: config.LOG_LEVEL
# Directs the logs to the terminal console using your environment's log level
logger.add(
    sys.stderr,
    level=settings.log_level.upper(),  # Python expects uppercase levels (e.g., 'INFO', 'DEBUG')
    format=log_format
)

# 4. Replaces: defaultMeta: {service: config.SERVICE_NAME}
# Injects the service name into the 'extra' context for every single log automatically
logger = logger.bind(service=settings.service_name)