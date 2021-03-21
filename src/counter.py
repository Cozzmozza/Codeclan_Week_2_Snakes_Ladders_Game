class Counter:
    def __init__(self, colour):
        self.colour = colour
        self.position = 0
    
    def update_position(self, number_of_spaces):
        self.position += number_of_spaces