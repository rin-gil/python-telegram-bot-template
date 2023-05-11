"""Tests for the filters.py module"""

from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from telegram import Chat, Message, User

from tgbot.utils.environment import env
from tgbot.utils.filters import IsAdmin


class IsAdminFilterTestCase(TestCase):
    """The unittest class for testing the filters module"""

    def setUp(self) -> None:
        """A setup method that will be called before each test case"""
        self._filter: IsAdmin = IsAdmin()
        self._admin_id: int = 123456789
        self._chat: Chat = Chat(id=1, type="private")
        self._date: datetime = datetime.now()

    def test_filter_returns_true_if_user_id_is_admin(self) -> None:
        """Filter test if the sender of the message is a bot administrator"""
        env.get_admin_ids = MagicMock(return_value=[self._admin_id])
        user: User = User(id=self._admin_id, first_name="Admin", is_bot=False)
        message: Message = Message(message_id=1, from_user=user, date=self._date, chat=self._chat)
        self.assertTrue(expr=self._filter.filter(message))

    def test_filter_returns_false_if_user_id_is_not_admin(self) -> None:
        """Filter test if the message sender is not a bot administrator"""
        non_admin_id: int = 987654321
        env.get_admin_ids = MagicMock(return_value=[self._admin_id])
        user: User = User(id=non_admin_id, first_name="Non-Admin", is_bot=False)
        message: Message = Message(message_id=1, from_user=user, date=self._date, chat=self._chat)
        self.assertFalse(expr=self._filter.filter(message))
