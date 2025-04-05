from unittest import TestCase
from game import check_for_foe
from unittest.mock import patch


class TestCheckForFoe(TestCase):
    @patch('game.random.random')
    def test_check_for_foe_true_level_2(self, mock_random):
        mock_random.return_value = 0.1
        character = {"Level": 2}
        expected = True
        actual = check_for_foe(character)
        self.assertEqual(expected, actual)

    @patch('game.random.random')
    def test_check_for_foe_false_level_2(self, mock_random):
        mock_random.return_value = 0.5
        character = {"Level": 2}
        expected = False
        actual = check_for_foe(character)
        self.assertEqual(expected, actual)

    @patch('game.random.random')
    def test_check_for_foe_true_level_3(self, mock_random):
        mock_random.return_value = 0.3
        character = {"Level": 3}
        expected = True
        actual = check_for_foe(character)
        self.assertEqual(expected, actual)

    @patch('game.random.random')
    def test_check_for_foe_false_level_3(self, mock_random):
        mock_random.return_value = 0.36
        character = {"Level": 3}
        expected = False
        actual = check_for_foe(character)
        self.assertEqual(expected, actual)
