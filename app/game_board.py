class GameBoard(object):

    # Global constants
    HIT = 'H'
    MISS = 'M'
    OCEAN = 'O'
    SHIP = 'S'

    def __init__(self):
        """
        Initialize the game board
        """

        self.board = self.load_board()

    def load_board(self):
        """
        Build a 10x10 grid for the game board

        :return: A list containing the grid for the game board
        """

        grid = []
        columns = [' ', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        rows = [('A', '|'), ('B', '|'), ('C', '|'), ('D', '|'), ('E', '|'), ('F', '|'), ('G', '|'), ('H', '|'),
                ('I', '|'), ('J', '|')]

        grid.append(columns)
        grid.append(['-'] * 12)
        for i in range(10):
            row = []
            row.extend(rows[i])
            row.extend([self.__class__.OCEAN] * 10)
            grid.append(row)

        return grid

    def show(self):
        """
        Display the players board to the screen
        """

        for row in self.board:
            print(' '.join(row))
