import unittest

from src.player import Player
from src.counter import Counter
from src.dice import Dice

class TestPlayer(unittest.TestCase):
    def setUp(self):
        counter = Counter('Yellow')
        self.player = Player('Bar John', counter, 30)

    def test_player_has_name(self):
        self.assertEqual('Bar John', self.player.name)

    def test_player_has_age(self):
        self.assertEqual(30, self.player.age)

    def test_player_has_counter_at_0(self):
        self.assertEqual(0, self.player.counter.position)
        # We are going through the player, get the counter attached to that player

    def test_player_can_roll_dice(self):
        dice = Dice(6)
        numbers = range (1,7) #Setting up a range of number possibilities
        self.assertIn(self.player.roll_dice(dice), numbers)
        # When I call roll_dice, with that dice defined, I expect a number in the numbers range
    
    def test_player_can_move_counter(self):
        self.player.move(7)
        self.assertEqual(7, self.player.counter.position)
