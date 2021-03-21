class Game:
    def __init__(self, board, dice, players):
        self.board = board
        self.dice = dice
        self.players = players
        self.is_won = False #Default
        self.current_player = players[0] #First player on the list

    def play(self): #Kick off the game
        # As long as the game isn't won, we want each player to take turns, in a loop
        # While game is not won:
        self.player_turn()          # Current player rolls dice and moves
        self.check_modifier()       # Check if they have landed on a modifier
        # Move if needed
        # Check if they have won
        self.rotate_player()        # Go to the next player
        # Repeat

    def player_turn(self):
        moves = self.current_player.roll_dice(self.dice)
        self.current_player.move(moves) #Updates the current players condition

    def check_modifier(self):
        current_position = self.current_player.counter.position 
        modifiers = self.board.modifiers
        if current_position in modifiers: # if the position is a snake or a ladder
            self.current_player.move(modifiers[current_position]) #Move by the key value paired value in the modifiers dictionary

    def rotate_player(self):
        number_of_players = len(self.players) # Finds the length of the players list
        current_index = self.players.index(self.current_player) #Finds the index number of the current player
        if current_index + 1 == number_of_players: # If the index number+1 is equal to the total number of players (so it doesn't run over)
            self.current_player = self.players[0] # Sets the current player back to player 1
        else:
            self.current_player = self.players[current_index + 1] # Else access player at the next index


    