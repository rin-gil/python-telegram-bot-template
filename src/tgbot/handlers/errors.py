"""
Handler of errors that are not caught by other functions

Writes an error message into the log, as well as the text of the message or callback from the user of the bot,
during the processing of which an error occurred
"""

import traceback

from telegram import Update
from telegram.ext import ContextTypes
from tgbot.utils.logger import logger


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs exceptions that are not handled by other functions"""
    traceback_list: list[str] = traceback.format_exception(None, context.error, context.error.__traceback__)
    if isinstance(update, Update) and update.message:
        message_or_callback_from_user: str = f", Message: {update.message.text}"
    elif isinstance(update, Update) and update.callback_query:
        message_or_callback_from_user = f", Callback: {update.callback_query.data}"
    else:
        message_or_callback_from_user = ""
    logger.error("Exception while handling an update: %s%s", traceback_list[-1].rstrip(), message_or_callback_from_user)
