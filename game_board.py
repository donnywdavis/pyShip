__author__ = 'donnywdavis'
__project__ = 'Battleship'

from random import randint

# Class to hold variables and methods
# needed for preparing and displaying the
# game board


class GameBoard(object):

    # Global variables
    HIT = "H"
    MISS = "X"
    OCEAN = "O"
    SHIP = "S"

    # Initialize the class
    def __init__(self, size, turns):
        self.size = size
        self.turns = turns
        # initialize the grid to the size specified
        self.grid = []
        for i in range(size):
            self.grid.append([self.OCEAN] * size)
        self.length = len(self.grid)
        self.ships = {}
        self.ship_positions = {}

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
        if self.grid[row][column] != self.OCEAN:
            return True
        else:
            return False

    # Update point on the board for a hit
    def mark_hit(self, row, column):
        self.grid[row][column] = self.HIT
        ship = self.get_ship_name([row, column])
        self.ships[ship]["hits"] += 1
        if self.ships[ship]["hits"] == self.ships[ship]["length"]:
            print("You sank the %s" % ship)
        print("Boom!")

    # Update point on the board for a miss
    def mark_miss(self, row, column):
        self.grid[row][column] = self.MISS
        print("Miss!")

    # Update point on the board to show a ship position
    def mark_ship_position(self, row, column):
        self.grid[row][column] = self.SHIP

    # Check if a given position is a hit or not
    def position_is_a_hit(self, row, column):
        if self.grid[row][column] == self.HIT:
            return True
        else:
            return False

    # Add ships to the board
    def add_ship(self, name, length):
        self.ships.__setitem__(name, {})
        self.ship_positions.__setitem__(name, [])
        self.ships[name].__setitem__("length", length)
        self.ships[name].__setitem__("hits", 0)
        self.ship_positions.__setitem__(name, self.set_ship_position(length))

    # Set the positions of the ship on the board
    def set_ship_position(self, length):
        ship_position = []
        while self.position_in_use(ship_position):
            start = [randint(0, (self.length - 1) - length), randint(0, self.length - 1)]
            if start[1] + length > 10:
                ship_position = [[x, start[1]] for x in range(start[0], (length + start[0]))]
            else:
                ship_position = [[start[0], y] for y in range(start[1], (length + start[1]))]
        else:
            return ship_position

    # Check that position has not already been used for another ship
    def position_in_use(self, position):
        if not position:
            return True

        for ship in self.ship_positions.keys():
            if position in self.ship_positions[ship]:
                return True
        else:
            return False

    # Check if we get a hit from the selection
    def hit_detected(self, selection):
        for ship in self.ship_positions:
            if selection in self.ship_positions[ship]:
                return True
        return False

    # Get ship name for a given position
    def get_ship_name(self, position):
        for ship in self.ship_positions:
            if position in self.ship_positions[ship]:
                return ship
        else:
            return ""