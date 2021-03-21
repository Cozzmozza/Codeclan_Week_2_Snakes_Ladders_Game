import random
# This is a python random package

class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def get_number(self):
        return random.randint(1,6)
    