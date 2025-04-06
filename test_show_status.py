import unittest
from io import StringIO
from unittest.mock import patch
from game import show_status


class TestShowStatus(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_show_status_output(self, fake_output):
        character = {
            "X": 1,
            "Y": 2,
            "HP": 3,
            "Max HP": 5,
            "Level": 2,
            "XP": 4,
            "XP to next": 6
        }

        expected = (
            "\033[94m\n=== Player Status ===\033[0m\n"
            "X: 1\n"
            "Y: 2\n"
            "HP: 3\n"
            "Max HP: 5\n"
            "Level: 2\n"
            "XP: 4\n"
            "XP to next: 6\n"
            "\033[94m\n=====================\033[0m\n"
        )
        show_status(character)
        actual = fake_output.getvalue()
        self.assertEqual(actual, expected)
