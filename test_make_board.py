import unittest
from unittest.mock import patch
from game import make_board


class TestMakeBoard(unittest.TestCase):
    @patch('game.random.choice')
    def test_make_board_type(self, mock_choice):
        mock_choice.return_value = "room"
        board = make_board(3, 3)
        self.assertIsInstance(board, dict)

    @patch('game.random.choice')
    def test_make_board_length(self, mock_choice):
        mock_choice.return_value = "room"
        board = make_board(2, 2)
        self.assertEqual(len(board), 4)

    @patch('game.random.choice')
    def test_make_board_coordinates(self, mock_choice):
        mock_choice.return_value = "room"
        rows, cols = 2, 2
        board = make_board(rows, cols)
        expected_keys = {(0, 0), (0, 1), (1, 0), (1, 1)}
        self.assertEqual(set(board.keys()), expected_keys)

    @patch('game.random.choice')
    def test_make_board_descriptions(self, mock_choice):
        mock_choice.return_value = "Test Room"
        board = make_board(1, 1)
        self.assertEqual(board[(0, 0)], "Test Room")
