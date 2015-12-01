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
        """
        Check if the player has any ships remaining

        :return: Boolean if there are ships remaining
        """

        return True if self.remaining_ships > 0 else False

    def check_for_hit(self, x, y):
        """
        Check if the selected position is a hit or not

        :param x: The x coordinate of the position
        :param y: The y coordinate of the position
        :return: Boolean if the ship is hit or not
        """

        for ship in self.ships:
            if ship.hit(x, y):
                self.board.mark_hit(x, y)
                if ship.sunk():
                    self.remaining_ships -= 1
                return True
            else:
                self.board.mark_miss(x, y)
                return False
