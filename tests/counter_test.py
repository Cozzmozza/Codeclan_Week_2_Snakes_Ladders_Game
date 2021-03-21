import unittest

from src.counter import Counter

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter('Red')

    def test_counter_colour(self):
        self.assertEqual('Red', self.counter.colour)

    def test_counter_position_starts_at_0(self):
        self.assertEqual(0, self.counter.position)

    def test_move_6_sets_position_6(self):
        self.counter.update_position(6)
        self.assertEqual(6, self.counter.position)

    def test_can_move_backwards(self):
        self.counter.update_position(30)
        self.counter.update_position(-7)
        self.assertEqual(23, self.counter.position)