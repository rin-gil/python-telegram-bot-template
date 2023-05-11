"""Tests for the bot_commands.py module"""

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, MagicMock, patch

from telegram import BotCommand
from telegram.ext import Application

from tgbot.utils.bot_commands import set_default_commands


class TestSetDefaultCommands(IsolatedAsyncioTestCase):
    """The unittest class for testing the bot_commands module"""

    def setUp(self) -> None:
        """Method initializes dummy objects needed to execute the tests"""
        self._application: MagicMock = MagicMock(spec=Application)

    async def test_set_default_commands(self) -> None:
        """
        The test verifies that the set_default_commands function forms the command list correctly
        and calls the set_my_commands method with the correct arguments.
        """
        expected_commands: list[BotCommand] = [
            BotCommand(command="start", description="▶️ Starts the bot"),
            BotCommand(command="help", description="ℹ️ Bot info"),
        ]

        bot_mock: MagicMock = MagicMock()
        bot_mock.set_my_commands = AsyncMock()
        self._application.bot = bot_mock

        with patch.object(target=Application, attribute="bot", new=bot_mock):
            await set_default_commands(application=self._application)

        bot_mock.set_my_commands.assert_awaited_once_with(commands=expected_commands, scope=None, language_code=None)
