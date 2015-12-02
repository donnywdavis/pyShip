from colorama import init, Fore

init()


class GameBoard(object):

    # Global constants
    HIT = Fore.RED + 'H' + Fore.RESET
    MISS = Fore.CYAN + 'M' + Fore.RESET
    OCEAN = Fore.BLUE + 'O' + Fore.RESET
    SHIP = Fore.WHITE + 'S' + Fore.RESET

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
        columns = [Fore.WHITE + ' ', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        rows = [(Fore.WHITE + 'A', '|'), (Fore.WHITE + 'B', '|'), (Fore.WHITE + 'C', '|'), (Fore.WHITE + 'D', '|'),
                (Fore.WHITE + 'E', '|'), (Fore.WHITE + 'F', '|'), (Fore.WHITE + 'G', '|'), (Fore.WHITE + 'H', '|'),
                (Fore.WHITE + 'I', '|'), (Fore.WHITE + 'J', '|')]

        grid.append(columns)
        grid.append([Fore.WHITE + '-'] * 12)
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

    def show_remaining(self, ships):
        """
        Display the remaining ships on the board

        :param ships: list for all of the ships on the board
        """

        for ship in ships:
            for position in ship.positions:
                if self.board[position[0]][position[1]] == self.__class__.OCEAN:
                    self.board[position[0]][position[1]] = self.__class__.SHIP

        self.show()

    def mark_hit(self, row, column):
        """
        Mark a position on the board as a hit

        :param row: The x coordinate for the position
        :param column: The y coordinate for the position
        """

        self.board[row][column] = self.__class__.HIT

    def mark_miss(self, row, column):
        """
        Mark a position on the board as a miss

        :param row: The x coordinate of the position
        :param column: The y coordinate of the position
        """

        self.board[row][column] = self.__class__.MISS

    def position_is_valid(self, row, column):
        """
        Check that a valid position on the board was selected

        :param row: The x coordinate of the position
        :param column: The y coordinate of the position
        :return: Boolean if the position is valid or not
        """

        if not row:
            return False

        if not column:
            return False

        try:
            row = self.convert_row(row)
        except KeyError:
            return False

        try:
            column = int(column) + 1
        except ValueError:
            return False

        if row > 11:
            return False

        if column > 11:
            return False

        return True if self.board[row][column] == self.__class__.OCEAN else False

    @staticmethod
    def convert_row(row):
        """
        Convert the selected row from a character to a numeric value

        :param row: The row letter to be converted
        :return: The numeric value for the selected row
        """

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
            'J': 11
        }

        return row_number[row.upper()]
