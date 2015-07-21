__author__ = 'donnywdavis'
__project__ = 'pyShip'

from player import Player


players = []


def setup_players():
    """
    Perform operations to set up the players that are going to play
    :return:
    """

    number_of_players = 0
    while number_of_players not in (1, 2):
        number_of_players = int(input('Select 1 or 2 players: '))
        if number_of_players not in (1, 2):
            print('Number of players must be 1 or 2')
    else:
        Player.number_of_players = number_of_players

    print('\nEnter player names:')
    index = 1
    while index <= Player.number_of_players:
        players.append(Player(index, input('Player {0}: '.format(index))))
        index += 1

    if Player.number_of_players < 2:
        players.append(Player(2, 'Computer'))


def main():
    """
    Main function for the program
    """

    print("Would you like to play a game?\n")

    setup_players()


if __name__ == '__main__':
    main()
