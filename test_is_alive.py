import unittest
from game import is_alive


class TestIsAlive(unittest.TestCase):

    def test_alive_positive_hp(self):
        character = {"HP": 5}
        expected = True
        actual = is_alive(character)
        self.assertEqual(actual, expected)

    def test_dead_zero_hp(self):
        character = {"HP": 0}
        expected = False
        actual = is_alive(character)
        self.assertEqual(actual, expected)

    def test_dead_negative_hp(self):
        character = {"HP": -3}
        expected = False
        actual = is_alive(character)
        self.assertEqual(actual, expected)
