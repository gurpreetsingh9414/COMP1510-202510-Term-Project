import unittest
from unittest.mock import patch
from game import rock_paper_scissors


class TestRockPaperScissors(unittest.TestCase):

    @patch("builtins.input", return_value="rock")
    @patch("random.choice", return_value="scissors")
    def test_player_wins(self, _, __):
        character = {"HP": 5, "XP": 0, "Level": 1, "XP to next": 3, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 5
        expected_xp = 2
        rock_paper_scissors(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="rock")
    @patch("random.choice", return_value="paper")
    def test_player_loses(self, _, __):
        character = {"HP": 3, "XP": 5, "Level": 2, "XP to next": 6, "Max HP": 6, "X": 0, "Y": 0}
        expected_hp = 2
        expected_xp = 5
        rock_paper_scissors(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="paper")
    @patch("random.choice", return_value="paper")
    def test_player_ties(self, _, __):
        character = {"HP": 4, "XP": 6, "Level": 2, "XP to next": 8, "Max HP": 6, "X": 0, "Y": 0}
        expected_hp = 4
        expected_xp = 6
        rock_paper_scissors(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)

    @patch("builtins.input", return_value="rocks")
    @patch("random.choice", return_value="rock")
    def test_invalid_input(self, _, __):
        character = {"HP": 3, "XP": 1, "Level": 1, "XP to next": 3, "Max HP": 5, "X": 0, "Y": 0}
        expected_hp = 2
        expected_xp = 1
        rock_paper_scissors(character)
        actual_hp = character["HP"]
        actual_xp = character["XP"]
        self.assertEqual(actual_hp, expected_hp)
        self.assertEqual(actual_xp, expected_xp)
