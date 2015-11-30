import unittest
from app.player import Player


class PlayerSetupTests(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(1, 'Player 1')
        self.player2 = Player(2, 'Computer')

    def test_player1_has_a_name(self):
        self.assertNotEqual(self.player1.name, '')

    def test_player1_game_board_generated(self):
        self.assertNotEqual(self.player1.board, None)

    def test_player2_has_a_name(self):
        self.assertNotEqual(self.player2.name, '')

    def test_player2_game_board_generated(self):
        self.assertNotEqual(self.player2.board, None)
