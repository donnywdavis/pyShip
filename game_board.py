__author__ = 'donnywdavis'

# Class to hold variables and methods
# needed for preparing and displaying the
# game board


class GameBoard(object):

    # Global class variables
    grid = []
    length = 0

    # Initialize the class
    def __init__(self, size):
        self.size = size
        # initialize the grid to the size specified
        for i in range(size):
            self.grid.append(["O"] * size)
        self.length = len(self.grid)

    # Draw the game board
    def draw(self):
        for row in self.grid:
            print(" ".join(row))