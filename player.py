__author__ = 'donnywdavis'
__project__ = 'pyShip'

from game_board import GameBoard


class Player(object):

    def __init__(self, player_number, name):
        self.player_number = player_number
        self.name = name
        self.board = GameBoard()
