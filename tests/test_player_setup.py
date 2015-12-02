import unittest
from app.player import Player


class PlayerSetupTests(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, 'Player 1', 2)
        self.player2 = Player(2, 'Player 2', 2)

    def test_player_has_a_name(self):
        self.assertNotEqual(self.player.name, '')

    def test_player_game_board_generated(self):
        self.assertNotEqual(self.player.board, None)

    def test_player_has_ships_generated(self):
        self.assertNotEqual(self.player, None)

    def test_player_has_correct_number_of_ships(self):
        self.assertEqual(len(self.player.ships), 2)

    def test_both_players_have_the_same_ships_loaded(self):
        player1_ships = [self.player.ships[i].name for i in range(len(self.player.ships))]
        player2_ships = [self.player2.ships[i].name for i in range(len(self.player2.ships))]
        self.assertListEqual(player1_ships, player2_ships)

    def test_player_has_ships_remaining(self):
        self.assertTrue(self.player.has_remaining_ships())

    def test_player_has_no_ships_remaining(self):
        self.player.remaining_ships = 0
        self.assertFalse(self.player.has_remaining_ships())

    def test_get_ship_at_selected_position(self):
        ship_position = self.player.ships[0].positions[0]
        self.assertNotEqual(self.player.get_ship(ship_position[0], ship_position[1]), None)
