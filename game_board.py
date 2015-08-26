__author__ = 'donnywdavis'
__project__ = 'pyShip'

from random import randint


used_positions = []
row_number = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6,
    'F': 7,
    'G': 8,
    'H': 9,
    'I': 10,
    'K': 11
}


def position_in_use(positions):
    """
    Check if a group of positions is already in use for another ship
    :param positions: A tuple containing potential positions for the current ship
    :return: Boolean value of whether any of the positions are in use
    """

    if not positions:
        return True

    for position in positions:
        if position in used_positions:
            return True
    used_positions.extend(positions)
    return False


def set_ship_position(ships):
    """
    Calculate the positions of each ship on the board
    :param ships: Dictionary of available ships
    :return: The dictionary of ships with set positions
    """

    for ship, attr in ships.items():
        positions = tuple()
        while position_in_use(positions):
            start = (randint(2, (11 - attr['length'])), randint(2, 11))
            if start[1] + attr['length'] > 11:
                positions = tuple([(x, start[1]) for x in range(start[0], (attr['length'] + start[0]))])
            else:
                positions = tuple([(start[0], y) for y in range(start[1], (attr['length'] + start[1]))])
        else:
            attr['positions'] = positions

    return ships


class GameBoard(object):
    """
    Class to hold variables and methods
    needed for preparing and displaying the
    game board
    """

    # Global variables
    HIT = "H"
    MISS = "X"
    OCEAN = "O"
    SHIP = "S"

    def __init__(self):
        """
        Initialize the GameBoard class
        """

        self.board = self.build_board()
        self.ships = self.load_ships()

    def build_board(self):
        """
        Build the game board grid with 10 rows and 10 columns
        :return: A list containing the rows and columns of the board
        """

        grid = []
        row_letter = [('A', '|'), ('B', '|'), ('C', '|'), ('D', '|'), ('E', '|'), ('F', '|'), ('H', '|'), ('I', '|'),
                      ('J', '|'), ('K', '|')]
        column_number = [' ', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        grid.append(column_number)
        grid.append(['-'] * 12)
        for i in range(10):
            row = []
            row.extend(row_letter[i])
            row.extend([self.OCEAN] * 10)
            grid.append(row)

        return grid

    def draw(self):
        """
        Print the game board to the screen
        """

        for row in self.board:
            print(' '.join(row))

    @staticmethod
    def load_ships():
        """
        Build dictionary of ships and their attributes
        :return: Dictionary of ships
        """

        ships = {
            'battleship': {
                'length': 4,
                'hits': 0,
                'positions': tuple()
            },
            'carrier': {
                'length': 6,
                'hits': 0,
                'positions': tuple()
            },
            'submarine': {
                'length': 3,
                'hits': 0,
                'positions': tuple()
            },
            'destroyer': {
                'length': 3,
                'hits': 0,
                'positions': tuple()
            },
            'cruiser': {
                'length': 2,
                'hits': 0,
                'positions': tuple()
            }
        }

        ships = set_ship_position(ships)

        return ships

    def check_for_hit(self, row, column):
        """
        Check if the selected position is a hit or a miss
        :param row: The row of the selection
        :param column: The column of the selection
        """
        for ship, attr in self.ships.items():
            if (row_number[row], column) in attr['positions']:
                self.board[row_number[row]][(column + 1)] = self.HIT
                print("\nBOOM! You got a hit.\n")
                break
        else:
            self.board[row_number[row]][(column + 1)] = self.MISS
            print("\nOops, no boom! You missed.\n")
