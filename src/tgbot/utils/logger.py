"""
The module provides logging settings for the bot

If DEBUG=True, the logs are written to the console in a more detailed form, otherwise they are written to the file
The path to the log file is set with the LOG_FILE constant

Example:
    Import logger:
        from tgbot.utils.logger import logger

    Logging events:
        logger.info("Starting bot")
        try:
            ...
        except Exception as exc:
            logger.critical("Critical error: %s", repr(exc))
"""

import logging
import sys

from tgbot.config import DEBUG, LOG_FILE


# Disables full traceback of errors in the log file
if not DEBUG:
    sys.tracebacklimit = 0

# logger config
logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=None if DEBUG else LOG_FILE,
    encoding="utf-8",
    format=f"[%(asctime)s] %(levelname)-8s {'%(filename)s:%(lineno)d - ' if DEBUG else ''}%(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
