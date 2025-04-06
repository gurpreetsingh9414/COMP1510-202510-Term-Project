import unittest
from game import move_character

class TestMoveCharacter(unittest.TestCase):

    def test_move_north(self):
        character = {"X": 2, "Y": 2}
        move_character(character, "north")
        expected = {"X": 1, "Y": 2}
        actual = character
        self.assertEqual(actual, expected)

    def test_move_south(self):
        character = {"X": 2, "Y": 2}
        move_character(character, "south")
        expected = {"X": 3, "Y": 2}
        actual = character
        self.assertEqual(actual, expected)

    def test_move_east(self):
        character = {"X": 2, "Y": 2}
        move_character(character, "east")
        expected = {"X": 2, "Y": 3}
        actual = character
        self.assertEqual(actual, expected)

    def test_move_west(self):
        character = {"X": 2, "Y": 2}
        move_character(character, "west")
        expected = {"X": 2, "Y": 1}
        actual = character
        self.assertEqual(actual, expected)



