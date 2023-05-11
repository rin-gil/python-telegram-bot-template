"""Tests for the logger.py module"""

import logging
import sys
from unittest import TestCase

from tgbot.utils import logger as logging_settings


class TestLoggingSettings(TestCase):
    """Tests for the logging settings module"""

    def test_logger(self) -> None:
        """Test that the logger object is an instance of logging.Logger"""
        self.assertIsInstance(obj=logging_settings.logger, cls=logging.Logger)

    def test_logging_file(self) -> None:
        """Test that the logging file is set correctly depending on the value of DEBUG"""
        if logging_settings.DEBUG:
            self.assertIsNone(obj=logging_settings.logging.getLogger().handlers[0].__dict__.get("baseFilename"))
        else:
            self.assertEqual(
                first=logging_settings.LOG_FILE,
                second=logging_settings.logging.getLogger().handlers[0].__dict__.get("baseFilename"),
            )

    def test_logging_format(self) -> None:
        """Test that the logging format is set correctly depending on the value of DEBUG"""
        expected_format: str = "[%(asctime)s] %(levelname)-8s %(name)s - %(message)s"
        if logging_settings.DEBUG:
            expected_format = "[%(asctime)s] %(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s"
        # pylint: disable=protected-access
        self.assertEqual(first=expected_format, second=logging_settings.logging.getLogger().handlers[0].formatter._fmt)

    def test_logging_level(self) -> None:
        """Test that the logging level is set to logging.INFO"""
        self.assertEqual(first=logging.INFO, second=logging_settings.logger.getEffectiveLevel())

    def test_tracebacklimit(self) -> None:
        """Test that sys.tracebacklimit is set to 0 if DEBUG is False"""
        if not logging_settings.DEBUG:
            self.assertEqual(first=0, second=sys.tracebacklimit)
