import unittest
from game import validate_move


class TestValidateMove(unittest.TestCase):

    def setUp(self):
        self.board = {
            (0, 0): "Start",
            (0, 1): "Right",
            (1, 0): "Down"
        }

    def test_validate_move_north_invalid(self):
        character = {"X": 0, "Y": 0}
        expected = False
        actual = validate_move(character, "north", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_south_valid(self):
        character = {"X": 0, "Y": 0}
        expected = True
        actual = validate_move(character, "south", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_east_valid(self):
        character = {"X": 0, "Y": 0}
        expected = True
        actual = validate_move(character, "east", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_west_invalid(self):
        character = {"X": 0, "Y": 0}
        expected = False
        actual = validate_move(character, "west", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_north_valid(self):
        character = {"X": 2, "Y": 2}
        expected = False
        actual = validate_move(character, "north", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_south_invalid(self):
        character = {"X": 4, "Y": 4}
        expected = False
        actual = validate_move(character, "south", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_east_invalid(self):
        character = {"X": 4, "Y": 4}
        expected = False
        actual = validate_move(character, "east", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_west_valid(self):
        character = {"X": 4, "Y": 4}
        expected = False
        actual = validate_move(character, "west", self.board)
        self.assertEqual(actual, expected)

    def test_validate_move_invalid_direction(self):
        character = {"X": 2, "Y": 2}
        expected = False
        actual = validate_move(character, "diagonal", self.board)
        self.assertEqual(actual, expected)


