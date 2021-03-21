import unittest

from src.dice import Dice
from src.board import Board
from src.counter import Counter 
from src.player import Player
from src.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        dice = Dice(6)
        counter_1 = Counter('Red')
        counter_2  = Counter('Yellow')
        player_1 = Player('Peter', counter_1, 27)
        player_2 = Player('Anna', counter_2, 21)
        modifiers = {
            3: 16,
            26: 28,
            32: 18,
            24: -18,
            35: -19,
            62: -25
        }
        board = Board(64, modifiers)

        self.game = Game(board, dice, [player_1, player_2])
    
    def test_game_not_won(self):
        self.assertFalse(self.game.is_won) #Just takes in one argument

    def test_current_player_is_player_1(self):
        self.assertEqual('Peter', self.game.current_player.name)