import unittest
from colorama import init, Fore
from app.game_board import GameBoard
import string
import random

init()


class GameBoardSetupTests(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()

    def test_game_board_generated(self):
        self.assertNotEqual(self.board, None)

    def test_game_board_has_10_by_10_grid(self):
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
            row.extend([self.board.__class__.OCEAN] * 10)
            grid.append(row)

        self.assertListEqual(self.board.board, grid)

    def test_valid_position_selected(self):
        self.assertTrue(self.board.position_is_valid(random.choice(string.ascii_uppercase[:10]), 5))

    def test_invalid_row_selected(self):
        self.assertFalse(self.board.position_is_valid('K', 5))

    def test_no_row_selected(self):
        self.assertFalse(self.board.position_is_valid('', 5))

    def test_invalid_character_selected_for_row(self):
        self.assertFalse(self.board.position_is_valid('@', 5))

    def test_invalid_column_selected(self):
        self.assertFalse(self.board.position_is_valid(random.choice(string.ascii_uppercase[:10]), 11))

    def test_no_column_selected(self):
        self.assertFalse(self.board.position_is_valid(random.choice(string.ascii_uppercase[:10]), ''))

    def test_invalid_character_selected_for_column(self):
        self.assertFalse(self.board.position_is_valid(random.choice(string.ascii_uppercase[:10]), 'A'))

    def test_position_marked_as_hit(self):
        self.board.mark_hit(5, 5)
        self.assertEqual(self.board.board[5][5], self.board.__class__.HIT)

    def test_position_marked_as_miss(self):
        self.board.mark_miss(5, 5)
        self.assertEqual(self.board.board[5][5], self.board.__class__.MISS)
