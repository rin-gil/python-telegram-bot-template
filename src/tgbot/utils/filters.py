"""
The module contains various filters that can be used in handlers

Example:
    Import the filter into the module with handlers:
        from tgbot.utils.filters import is_admin_filter

    Create a handler, which must respond to the command /start if the sender of the message is a bot administrator:
        async def start_cmd_from_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text(text="Hello, admin!")
        start_cmd_from_admin_handler: CommandHandler = CommandHandler(
            command="start", callback=start_cmd_from_admin, filters=is_admin_filter
        )

    Let's add a handler to the application:
        application.add_handler(handler=start_cmd_from_admin_handler)

More info: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Advanced-Filters
"""

from telegram import Message
from telegram.ext.filters import MessageFilter

from tgbot.utils.environment import env


class IsAdmin(MessageFilter):
    """The filter allows you to determine if the sender of the message is a bot administrator"""

    def filter(self, message: Message) -> bool:
        """
        Checks if the message sender is a bot administrator

        :param message: Message class object
        :type message: Message
        :return: True or False
        :rtype: bool
        """
        return message.from_user.id in env.get_admin_ids()


is_admin_filter = IsAdmin()
