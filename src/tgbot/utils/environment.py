"""
Module for reading values from environment variables in .env files
Contains Environment class, which performs reading of values and env - object of Environment class

Example:
    Import an instance of the class into the desired module:
        from tgbot.utils.environment import env

    Get the values from the environment variables:
        bot_token: str = env.get_token_or_exit()
        bot_admins: tuple[int, ...] = env.get_admin_ids_or_exit()
"""

from os import path
from sys import exit as sys_exit

from environs import Env, EnvError

from tgbot.config import ENV_FILE
from tgbot.utils.logger import logger


class Environment:
    """Reads variables from the .env file"""

    def __init__(self, path_to_env_file: str) -> None:
        """
        Initializing a class or terminating a program if no .env file is found

        :param path_to_env_file: path to .env file with environment variables
        :type path_to_env_file: str
        """
        if not path.exists(path=path_to_env_file):
            logger.critical("The .env file was not found in the path %s", path_to_env_file)
            sys_exit(1)
        self._env: Env = Env()
        self._env.read_env(path=path_to_env_file, recurse=False)

    def get_token_or_exit(self) -> str:
        """
        Returns the bot token or terminates the program in case of an error

        :return: bot token
        :rtype: str
        """
        try:
            return str(self._env.str("BOT_TOKEN"))
        except EnvError as exc:
            logger.critical("BOT_TOKEN not found: %s", repr(exc))
            sys_exit(repr(exc))

    def get_admin_ids(self) -> tuple[int, ...] | None:
        """
        Returns administrator IDs or None if ADMINS is not set in the .env file

        :return: admin ids
        :rtype: tuple[int, ...] | None
        """
        try:
            return tuple(map(int, self._env.list("ADMINS")))
        except (EnvError, ValueError) as exc:
            logger.error("ADMINS ids not found: %s", repr(exc))
            return None


env: Environment = Environment(path_to_env_file=ENV_FILE)
