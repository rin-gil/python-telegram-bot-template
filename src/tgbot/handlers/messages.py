"""
This module contains handlers that handle messages from users

Handlers:
    echo_handler    - echoes the user's message

Note:
    Handlers are imported into the __init__.py package handlers,
    where a tuple of HANDLERS is assembled for further registration in the application
"""

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message"""
    await update.message.reply_text(text=update.message.text, quote=True)


echo_handler: MessageHandler = MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=echo)
