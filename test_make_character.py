import unittest
from game import make_character

class TestMakeCharacter(unittest.TestCase):
    def test_return_type(self):
        character = make_character()
        self.assertIsInstance(character, dict)

    def test_default_stats(self):
        expected = {
            "X": 0,
            "Y": 0,
            "HP": 5,
            "Max HP": 5,
            "Level": 1,
            "XP": 0,
            "XP to next": 3,
        }
        actual = make_character()
        self.assertEqual(actual, expected)

    def test_hp_equals_max_hp(self):
        character = make_character()
        self.assertEqual(character["HP"], character["Max HP"])

    def test_starting_position(self):
        character = make_character()
        self.assertEqual((character["X"], character["Y"]), (0, 0))
