__author__ = 'donnywdavis'
__project__ = 'pyShip'

from random import randint


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
        row_letter = ['A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'H |', 'I |', 'J |', 'K |']
        column_number = [' ', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        grid.append(column_number)
        grid.append(['-'] * 12)
        for i in range(10):
            row = [row_letter[i]]
            row.extend([self.OCEAN] * 10)
            grid.append(row)

        return grid

    def draw(self):
        """
        Print the game board to the screen
        """

        for row in self.board:
            print(' '.join(row))

    def load_ships(self):
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

        return ships
