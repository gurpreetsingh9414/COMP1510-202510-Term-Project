import unittest
from unittest.mock import patch
from game import number_guessing_game


class TestNumberGuessingGame(unittest.TestCase):

    @patch("builtins.input", return_value="3")
    @patch("random.randint", return_value=3)
    def test_correct_guess(self, _, __):
        character = {"HP": 5, "XP": 0, "Level": 1, "XP to next": 3, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 5
        expected_xp = 2
        number_guessing_game(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="1")
    @patch("random.randint", return_value=2)
    def test_wrong_guess(self, _, __):
        character = {"HP": 3, "XP": 4, "Level": 2, "XP to next": 6, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 2
        expected_xp = 4
        number_guessing_game(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="not_a_number")
    @patch("random.randint", return_value=4)
    def test_invalid_input(self, _, __):
        character = {"HP": 2, "XP": 3, "Level": 1, "XP to next": 3, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 1
        expected_xp = 3
        number_guessing_game(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)
