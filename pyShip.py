__author__ = 'donnywdavis'
__project__ = 'pyShip'

from player import Player
from random import randint

row_letter = {
    2: 'A',
    3: 'B',
    4: 'C',
    5: 'D',
    6: 'E',
    7: 'F',
    8: 'G',
    9: 'H',
    10: 'I',
    11: 'J'
}


def setup_players():
    """
    Perform operations to set up the players that are going to play

    :return: List containing object for each player
    """

    players = []
    number_of_players = 0
    while number_of_players not in (1, 2):
        number_of_players = int(input('Select 1 or 2 players: '))
        if number_of_players not in (1, 2):
            print('Number of players must be 1 or 2')

    print('\nEnter player names:')
    index = 1
    while index <= number_of_players:
        players.append(Player(index, input('Player {0}: '.format(index))))
        index += 1

    if number_of_players < 2:
        players.append(Player(2, 'Computer'))

    return players


def main():
    """
    Main function for the program
    """

    print("Would you like to play a game?\n")

    players = setup_players()
    current_player = players[0]
    current_player_hold = players[0]
    next_player = players[1]
    game_on = True

    while game_on:
        print("\n{0}'s turn.\n".format(current_player.name))
        next_player.board.draw()
        if current_player.name == 'Computer':
            row = row_letter[randint(2, 11)]
            print("\nSelect a row: {0}".format(row))
            column = randint(1, 10)
            print("Select a column: {0}".format(column))
        else:
            row = input("\nSelect a row: ").upper()
            column = input("Select a column: ")
        if next_player.board.valid_position_selected(row, column):
            next_player.board.check_for_hit(row, int(column))

            if next_player.board.total_ships == next_player.board.ships_sunk:
                game_on = False
            else:
                # Swap players for the next round
                current_player = next_player
                next_player = current_player_hold
                current_player_hold = current_player
        else:
            print("\nSelected position is not valid. Please select again.\n")

    # Display all remaining ships for both players
    print("\nGame Over\n")
    print("{0} Wins".format(current_player.name))
    print("\n{0}'s board.\n".format(current_player.name))
    current_player.board.show_remaining_ships()

    print("\n{0}'s board.\n".format(next_player.name))
    next_player.board.show_remaining_ships()

if __name__ == '__main__':
    main()
