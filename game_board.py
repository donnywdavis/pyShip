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
