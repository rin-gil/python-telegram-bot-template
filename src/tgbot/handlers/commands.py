"""
The module contains handlers that respond to commands from bot users

Handlers:
    start_cmd_from_admin_handler    - response to the /start command from the bot administrator
    start_cmd_from_user_handler     - response to the /start command from the bot user
    help_cmd_handler                - response to the /help command

Note:
    Handlers are imported into the __init__.py package handlers,
    where a tuple of HANDLERS is assembled for further registration in the application
"""

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from tgbot.config import BOT_LOGO
from tgbot.utils.filters import is_admin_filter
from tgbot.utils.templates import template


async def start_cmd_from_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles command /start from the admin"""
    await update.message.reply_text(text="👋 Hello, admin!")


async def start_cmd_from_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles command /start from the user"""
    username: str = update.message.from_user.first_name
    await update.message.reply_text(text=f"👋 Hello, {username if username else 'user'}!")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles command /help from the user

    Note:
        In this handler as an example, we will use the template renderer to format the response message
    """
    data: dict = {
        "framework_url": "https://python-telegram-bot.org",
        "licence_url": "https://github.com/rin-gil/python-telegram-bot-template/blob/master/LICENCE",
        "github_repo_url": "https://github.com/rin-gil/python-telegram-bot-template",
        "author_profile_url": "https://github.com/rin-gil",
        "author_email": "e.ringil@prothon.me",
    }
    caption: str = await template.render(template_name="help_cmd.jinja2", data=data)
    await update.message.reply_photo(photo=BOT_LOGO, caption=caption)


# Creating handlers
start_cmd_from_admin_handler: CommandHandler = CommandHandler(
    command="start", callback=start_cmd_from_admin, filters=is_admin_filter
)
start_cmd_from_user_handler: CommandHandler = CommandHandler(command="start", callback=start_cmd_from_user)
help_cmd_handler: CommandHandler = CommandHandler(command="help", callback=help_cmd)
