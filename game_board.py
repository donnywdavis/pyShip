__author__ = 'donnywdavis'
__project__ = 'pyShip'

from random import randint

"""
Class to hold variables and methods
needed for preparing and displaying the
game board
"""


class GameBoard(object):

    # Global variables
    HIT = "H"
    MISS = "X"
    OCEAN = "O"
    SHIP = "S"
    ships_sunk = 0

    def __init__(self, size, turns):
        """
        Initialization for the GameBoard class

        :param size: The size of the game board grid
        :param turns: The number of turns for the game
        :return:
        """

        self.size = size
        self.turns = turns
        # initialize the grid to the size specified
        self.grid = []
        for i in range(size):
            self.grid.append([self.OCEAN] * size)
        self.length = len(self.grid)
        self.ships = {}
        self.ship_positions = {}

    def draw(self):
        """
        Print the game board grid to the screen

        :return:
        """

        for row in self.grid:
            print(" ".join(row))

    def valid_selection(self, row, column):
        """
        Check if the selection was a valid point on the game board grid

        :param row: The row that the selection is for
        :param column: The column that the selection is for
        :return: False if the row or column is outside of the grid size
                 True if the row or column is inside the grid size
        """

        if row < 0 or row > (self.size - 1) or column < 0 or column > (self.size - 1):
            return False
        else:
            return True

    def position_already_selected(self, row, column):
        """
        Check if a position has already been selected

        :param row: The row that the selection is for
        :param column: The column that the selection is for
        :return: True if the selection has already been used
                 False if the selection has not been used
        """

        if self.grid[row][column] != self.OCEAN:
            return True
        else:
            return False

    def mark_hit(self, row, column):
        """
        Update the selected point on the grid as a hit

        :param row: The row that the selection is for
        :param column: The column that the selection is for
        :return:
        """

        self.grid[row][column] = self.HIT
        ship = self.get_ship_name((row, column))
        self.ships[ship]["hits"] += 1
        if self.ships[ship]["hits"] == self.ships[ship]["length"]:
            self.ships_sunk += 1
            print("You sank the %s" % ship)
        print("Boom!")

    def mark_miss(self, row, column):
        """
        Update the selected point on the grid as a miss

        :param row: The row that the selection is for
        :param column: The column that the selection is for
        :return:
        """

        self.grid[row][column] = self.MISS
        print("Miss!")

    def mark_ship_position(self, row, column):
        """
        Update the point on the grid as a ship

        :param row: The row that the point is for
        :param column: The column that the point is for
        :return:
        """

        self.grid[row][column] = self.SHIP

    def position_is_a_hit(self, row, column):
        """
        Check if a position on the grid is a hit

        :param row: The row that the position is for
        :param column: The column that the position is for
        :return: True if the position is a hit
                 False if the position is not a hit
        """

        if self.grid[row][column] == self.HIT:
            return True
        else:
            return False

    def add_ship(self, name, length):
        """
        Add a new ship to the game board grid

        :param name: The name of the ship
        :param length: The length of the ship
        :return:
        """
        self.ships.__setitem__(name, {})
        self.ship_positions.__setitem__(name, ())
        self.ships[name].__setitem__("length", length)
        self.ships[name].__setitem__("hits", 0)
        self.ship_positions.__setitem__(name, self.set_ship_position(length))

    def set_ship_position(self, length):
        """
        Calculate the positions for a ship on the game board based on the ships length

        :param length: The length of the ship
        :return: A list of points on the grid that the ship will occupy
        """

        ship_position = ()
        while self.position_in_use(ship_position):
            start = (randint(0, (self.length - 1) - length), randint(0, self.length - 1))
            if start[1] + length > 10:
                ship_position = tuple([(x, start[1]) for x in range(start[0], (length + start[0]))])
            else:
                ship_position = tuple([(start[0], y) for y in range(start[1], (length + start[1]))])
        else:
            return ship_position

    def position_in_use(self, position):
        """
        Check to see if a given position is currently in use by another ship

        :param position: A list containing row and column for a position
        :return: True if the position is being used or if no position is passed
                 False if the position is not being used
        """

        if not position:
            return True

        for ship in self.ship_positions.keys():
            if len(set(position) & set(self.ship_positions[ship])) > 0:
                return True
        else:
            return False

    def hit_detected(self, selection):
        """
        Check to see if we got a hit for the selected position

        :param selection: List containing row and column for a position on the grid
        :return:
        """

        for ship in self.ship_positions:
            if selection in self.ship_positions[ship]:
                return True
        return False

    def get_ship_name(self, position):
        """
        Get the ship name for a ship at a given position

        :param position: List containing row and column for a position on the grid
        :return:
        """

        for ship in self.ship_positions:
            if position in self.ship_positions[ship]:
                return ship
        else:
            return ""

    def show_all_ships(self):
        """
        Update the grid to show the position of all ships and print that to the screen

        :return:
        """

        for ship, positions in self.ship_positions.items():
            for position in positions:
                if not self.position_is_a_hit(position[0], position[1]):
                    self.mark_ship_position(position[0], position[1])
        self.draw()