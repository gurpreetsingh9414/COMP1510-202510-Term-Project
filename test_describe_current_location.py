import unittest
from unittest.mock import patch
from io import StringIO
from game import describe_current_location

green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
reset = "\033[0m"


class TestDescribeCurrentLocation(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_location_ashoka_chamber(self, mock_stdout):
        board = {
            (0,
             0): blue + "THE ASHOKA CHAMBER - Ancient inscriptions glow faintly on the sandstone walls. The air is heavy with the wisdom of Emperor Ashoka’s edicts.\nYou feel a strange pull — as if the Mauryan spirit still lingers here." + reset
        }
        character = {"X": 0, "Y": 0}
        expected = (
            f"\nYou are at (0, 0).\n"
            f"Location: {board[(0, 0)]}\n"
        )

        describe_current_location(board, character)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_location_trident_shrine(self, mock_stdout):
        board = {
            (1,
             2): green + "THE TRIDENT SHRINE - Three blazing torches illuminate a stone statue of Lord Shiva, his trident piercing the air above.\nEchoes of the Tandava dance resonate through the cold granite floor." + reset
        }
        character = {"X": 1, "Y": 2}
        expected = (
            f"\nYou are at (1, 2).\n"
            f"Location: {board[(1, 2)]}\n"
        )

        describe_current_location(board, character)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_location_dwarka_ruins(self, mock_stdout):
        board = {
            (2,
             3): cyan + "THE SUNKEN DWARKA RUINS - You tread through damp stone as ancient pillars rise from a waterlogged floor.\nA golden conch lies half-buried — perhaps once blown by Krishna himself before battle. The sea whispers stories of the lost city." + reset
        }
        character = {"X": 2, "Y": 3}
        expected = (
            f"\nYou are at (2, 3).\n"
            f"Location: {board[(2, 3)]}\n"
        )

        describe_current_location(board, character)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_location_agni_passage(self, mock_stdout):
        board = {
            (3,
             1): yellow + "THE AGNI PASSAGE - The walls pulse with heat, carved with flames and Vedic mantras.\nThis sacred tunnel is said to be blessed by Agni, the fire god. Only those with pure intent may pass unharmed." + reset
        }
        character = {"X": 3, "Y": 1}
        expected = (
            f"\nYou are at (3, 1).\n"
            f"Location: {board[(3, 1)]}\n"
        )

        describe_current_location(board, character)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
