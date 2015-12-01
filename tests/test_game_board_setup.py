import unittest
from app.game_board import GameBoard


class GameBoardSetupTests(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()

    def test_game_board_generated(self):
        self.assertNotEqual(self.board, None)

    def test_game_board_has_10_by_10_grid(self):
        grid = []
        columns = [' ', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        rows = [('A', '|'), ('B', '|'), ('C', '|'), ('D', '|'), ('E', '|'), ('F', '|'), ('G', '|'), ('H', '|'),
                ('I', '|'), ('J', '|')]
        grid.append(columns)
        grid.append(['-'] * 12)
        for i in range(10):
            row = []
            row.extend(rows[i])
            row.extend(['O'] * 10)
            grid.append(row)

        self.assertListEqual(self.board.board, grid)
