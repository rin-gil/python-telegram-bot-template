"""Setting up the configuration for the bot"""

from os.path import join, normpath
from pathlib import Path


# Change DEBUG to False when running on a production server
DEBUG: bool = True

# Path settings
_BASE_DIR: Path = Path(__file__).resolve().parent.parent
BOT_LOGO: str = normpath(join(_BASE_DIR, "tgbot/assets/img/bot_logo.jpg"))
ENV_FILE: str = normpath(join(_BASE_DIR, ".env"))
LOG_FILE: str = normpath(join(_BASE_DIR, "tgbot.log"))
TEMPLATES_DIR: str = normpath(join(_BASE_DIR, "tgbot/templates"))
