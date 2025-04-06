import unittest
from unittest.mock import patch
from game import riddle_game


class TestRiddleGame(unittest.TestCase):

    @patch("builtins.input", return_value="keyboard")
    @patch("random.choice", return_value=("What has keys but can't open locks?", "keyboard"))
    def test_correct_riddle_answer(self, _, __):
        character = {"HP": 3, "XP": 0, "Level": 1, "XP to next": 5, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 3
        expected_xp = 3

        riddle_game(character)

        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="key board")
    @patch("random.choice", return_value=("What has keys but can't open locks?", "keyboard"))
    def test_incorrect_riddle_answer(self, _, __):
        character = {"HP": 4, "XP": 2, "Level": 1, "XP to next": 6, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 3
        expected_xp = 2
        riddle_game(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

