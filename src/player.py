# from src.counter import Counter

class Player:
    def __init__(self, name, counter, age):
        self.name = name
        self.counter = counter
        self.age = age

    # def roll_dice(self, dice):
    # I can import random and tell the dice here to find a number
    # But this is wrong. We have a dice class already
    # All I need to do, is call the dice object

    def roll_dice(self, dice):
        return dice.get_number()

    def move(self, number):
        self.counter.update_position(number)
