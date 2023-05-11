"""Tests for the environments.py module"""

from unittest import TestCase
from unittest.mock import patch, MagicMock

from environs import EnvError

from tgbot.config import ENV_FILE
from tgbot.utils.environment import Environment


class TestEnvironment(TestCase):
    """Tests for the Environment class"""

    def setUp(self) -> None:
        """Create an instance of the Environment class"""
        self.env: Environment = Environment(path_to_env_file=f"{ENV_FILE}")

    @patch("environs.Env.str", MagicMock(return_value="123456:Your-TokEn_ExaMple"))
    def test_get_token_or_exit(self) -> None:
        """Test the get_token_or_exit method"""
        self.assertEqual(first=self.env.get_token_or_exit(), second="123456:Your-TokEn_ExaMple")

    @patch("environs.Env.list", MagicMock(return_value=["123456789", "23456789", "3456789"]))
    def test_get_admin_ids_or_exit(self) -> None:
        """Test the get_admin_ids_or_exit method"""
        self.assertEqual(first=self.env.get_admin_ids(), second=(123456789, 23456789, 3456789))

    @patch("environs.Env.str", MagicMock(side_effect=EnvError("BOT_TOKEN not found")))
    def test_get_token_or_exit_when_env_error(self) -> None:
        """Test the get_token_or_exit method when an EnvError occurs"""
        with self.assertRaises(expected_exception=SystemExit):
            self.env.get_token_or_exit()

    @patch("environs.Env.list", MagicMock(side_effect=EnvError("ADMINS not found")))
    def test_get_admin_ids_when_env_error(self) -> None:
        """Test the get_admin_ids_or_exit method when an EnvError occurs"""
        self.assertIsNone(obj=self.env.get_admin_ids())

    @patch("environs.Env.list", MagicMock(return_value=["123456789", 23456789, "three456789"]))
    def test_get_admin_ids_when_value_error(self) -> None:
        """Test the get_admin_ids_or_exit method when a ValueError occurs"""
        self.assertIsNone(obj=self.env.get_admin_ids())
