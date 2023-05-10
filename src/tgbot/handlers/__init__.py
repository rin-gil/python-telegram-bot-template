"""
The module contains event handlers in the bot.

Note:
    Error handlers cannot be passed with this tuple and must be registered separately:
        application.add_handlers(handlers=HANDLERS)
        application.add_error_handler(callback=error_handler)

Modules:
    callbacks.py    - handlers for user button presses
    commands.py     - command handlers from users
    messages.py     - user message handlers
    errors.py       - possible error handlers

Constants:
    HANDLERS - a tuple of handlers for further import and registration in the application
"""

from tgbot.handlers.commands import (
    start_cmd_from_admin_handler,
    start_cmd_from_user_handler,
    help_cmd_handler,
)
from tgbot.handlers.messages import echo_handler


HANDLERS: tuple = (  # the order of the elements is important
    start_cmd_from_admin_handler,
    start_cmd_from_user_handler,
    help_cmd_handler,
    echo_handler,
)
