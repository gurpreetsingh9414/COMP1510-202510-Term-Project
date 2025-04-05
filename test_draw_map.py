import unittest
from unittest.mock import patch
from io import StringIO
from game import draw_map


class TestDrawMap(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_starting_position(self, mock_stdout):
        character = {"X": 0, "Y": 0}
        draw_map(character)
        output = mock_stdout.getvalue()
        self.assertIn("[P]", output)
        self.assertIn("[F]", output)
        self.assertEqual(output.count("[P]"), 1)
        self.assertEqual(output.count("[F]"), 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_player_on_finish_position(self, mock_stdout):
        character = {"X": 4, "Y": 4}
        draw_map(character)
        output = mock_stdout.getvalue()
        self.assertIn("[P]", output)
        self.assertEqual(output.count("[P]"), 1)
        self.assertNotIn("[F]", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid_size(self, mock_stdout):
        character = {"X": 1, "Y": 1}
        draw_map(character, rows=3, columns=3)
        output = mock_stdout.getvalue()
        self.assertEqual(output.count("\n"), 5)
