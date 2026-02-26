from loguru import logger
import sys

def setup_logging(level="INFO"):
    logger.remove()
    logger.add(
        sys.stdout,
        level=level,
        format="<green>{time}</green> | <level>{level}</level> | {message}"
    )

    return logger
