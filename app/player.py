from app.game_board import GameBoard
from app.ship import load_ships


class Player(object):

    def __init__(self, player_number, name, number_of_ships=5):
        """
        Initialize the player object

        :param player_number: The number of the player
        :param name: The name of the player
        """

        self.player_number = player_number
        self.name = name
        self.board = GameBoard()
        self.remaining_ships = number_of_ships
        self.ships = load_ships(number_of_ships)

    def __str__(self):
        return self.name

    def has_remaining_ships(self):
        return True if self.remaining_ships > 0 else False
