import unittest

from src.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        modifiers = {
            3: 16,
            26: 28,
            32: 18,
            24: -18,
            35: -19,
            62: -25
        }
        self.board = Board(64, modifiers)

    def test_number_of_squares(self):
        self.assertEqual(64, self.board.number_of_squares)

    def test_can_get_modifiers(self):
        value = self.board.modifiers[26]
        self.assertEqual(28, value)