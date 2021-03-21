import unittest

from src.dice import Dice

class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice(6)
    
    def test_number_of_sides(self):
        self.assertEqual(6, self.dice.number_of_sides)

    def test_can_get_number(self):
        numbers = range(1,7)
        self.assertIn(self.dice.get_number(), numbers)
