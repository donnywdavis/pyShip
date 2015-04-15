__author__ = 'donnywdavis'

# Class to hold variables and methods
# needed for preparing and displaying the
# game board


class GameBoard(object):

    # Initialize the class
    def __init__(self, size, turns):
        self.size = size
        self.turns = turns
        # initialize the grid to the size specified
        self.grid = []
        for i in range(size):
            self.grid.append(["O"] * size)
        self.length = len(self.grid)

    # Draw the game board
    def draw(self):
        for row in self.grid:
            print(" ".join(row))

    # Check if a valid selection was made
    def valid_selection(self, row, column):
        if row < 0 or row > 9 or column < 0 or column > 9:
            return False
        else:
            return True

    # Check if the position has already been selected
    def position_already_selected(self, row, column):
        if self.grid[row][column] == "X":
            return True
        else:
            return False

    # Update point on the board for a hit
    def mark_hit(self, row, column):
        self.grid[row][column] = "H"
        print("Boom!")

    # Update point on the board for a miss
    def mark_miss(self, row, column):
        self.grid[row][column] = "X"
        print("Miss!")

    # Update point on the board to show a ship position
    def mark_ship_position(self, row, column):
        self.grid[row][column] = "S"

    # Check if a given position is a hit or not
    def position_is_a_hit(self, row, column):
        if self.grid[row][column] == "H":
            return True
        else:
            return False