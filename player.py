__author__ = 'donnywdavis'
__project__ = 'pyShip'

from game_board import GameBoard


def valid_number_of_players(number_of_players):
    """
    Validate the number of players entered

    :param number_of_players: The number of players entered
    :return: Boolean value whether it's valid or not
    """

    return True if number_of_players in ('1', '2') else False


def get_number_of_players():
    """
    Get the number of players

    :return: The number of players
    """

    number_of_players = ""
    while not valid_number_of_players(number_of_players):
        number_of_players = input('Select 1 or 2 players: ')
        if not valid_number_of_players(number_of_players):
            print('Number of players must be 1 or 2')

    return int(number_of_players)


def setup_players():
    """
    Create an object for each player

    :return: A list of player objects
    """

    players = []
    number_of_players = get_number_of_players()
    index = 1
    while index <= number_of_players:
        players.append(Player(index, 'Player {0}'.format(index)))
        index += 1

    if number_of_players < 2:
        players.append(Player(2, 'Computer'))

    return players


class Player(object):

    def __init__(self, player_number, name):
        self.player_number = player_number
        self.name = name
        self.board = GameBoard()
