"""Tests for the error_handler from errors.py module"""

import logging
from asyncio import new_event_loop, set_event_loop, AbstractEventLoop
from unittest import TestCase
from unittest.mock import Mock
from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.errors import error_handler
from tgbot.utils.logger import logger


logging.basicConfig(level=logging.ERROR)


class TestErrorHandler(TestCase):
    """The unittest class for error handler"""

    def setUp(self) -> None:
        """Method initializes dummy objects needed to execute the tests"""
        self._loop: AbstractEventLoop = new_event_loop()
        set_event_loop(None)
        self._update: Mock = Mock(spec=Update)
        self._context: Mock = Mock(spec=CallbackContext)
        self._update.message = None
        self._update.callback_query = None
        self._context.error = Exception("Test Exception")
        self._context.error.__traceback__ = None

    def tearDown(self) -> None:
        """Clears the resources that have been allocated to the test"""
        self._loop.close()

    def test_error_handler_logs_exception(self) -> None:
        """Checks that error_handler registers an exception"""
        with self.assertLogs(logger=logger, level="ERROR") as log:
            self._loop.run_until_complete(error_handler(update=self._update, context=self._context))
        self.assertIn("Exception while handling an update: Exception: Test Exception", log.output[0])

    def test_error_handler_logs_when_update_message(self) -> None:
        """Checks that the error_handler function registers an exception when handling the message"""
        self._update.message = Mock(text="Test Message")
        with self.assertLogs(logger=logger, level="ERROR") as log:
            self._loop.run_until_complete(error_handler(update=self._update, context=self._context))
        self.assertIn(
            "Exception while handling an update: Exception: Test Exception, Message: Test Message", log.output[0]
        )

    def test_error_handler_logs_when_update_callback(self) -> None:
        """Checks that the error_handler function registers an exception when handling the callback"""
        self._update.callback_query = Mock(data="Test Callback")
        with self.assertLogs(logger=logger, level="ERROR") as log:
            self._loop.run_until_complete(error_handler(update=self._update, context=self._context))
        self.assertIn(
            "Exception while handling an update: Exception: Test Exception, Callback: Test Callback", log.output[0]
        )
