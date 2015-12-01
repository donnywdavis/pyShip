#!/usr/bin/env python
import argparse
from app.player import Player
import string
import random


def main():
    """
    Main function for the game
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--number_of_players', help="The number of players playing the game.", type=int,
                        choices=[1, 2], default=1)
    parser.add_argument('-s', '--number_of_ships', help="The number of ships for each player.", type=int,
                        choices=[2, 3, 4, 5], default=5)
    args = parser.parse_args()

    # Let's set up our players
    player1 = Player(1, 'Player 1', args.number_of_ships)
    if args.number_of_players > 1:
        player2 = Player(2, 'Player 2', args.number_of_ships)
    else:
        player2 = Player(2, 'Computer', args.number_of_ships)

    current_player = player1
    hold_current_player = player1
    next_player = player2
    game_on = True

    print("Welcome to pyShip!")
    print("=" * 24)

    while game_on:
        print("\n{0}'s turn.".format(current_player.name))
        print("=" * 24)
        next_player.board.show()
        print("\n")

        row = ''
        column = ''
        if current_player.name == 'Computer':
            while not next_player.board.position_is_valid(row, column):
                row = random.choice(string.ascii_uppercase[:10])
                column = random.randint(1, 10)
            print("Select a row: {0}".format(row))
            print("Select a column: {0}".format(column))
        else:
            while not next_player.board.position_is_valid(row, column):
                row = input("Select a row: ").upper()
                column = input("Select a column: ")

        row = current_player.board.convert_row(row)
        column = int(column) + 1

        print("\n")

        if next_player.check_for_hit(row, column):
            print("BOOM! You got a hit.")
            if not next_player.has_remaining_ships():
                game_on = False
        else:
            print("MISS! No boom for you.\n")

        current_player = next_player
        next_player = hold_current_player
        hold_current_player = current_player

        print("=" * 24)

    print("\nGame Over\n")
    print("{0} Wins.\n".format(current_player.name))
    print("{0}'s board:\n".format(current_player.name))
    current_player.board.show_remaining(current_player.ships)
    print("\n{0}'s board:\n".format(next_player.name))
    next_player.board.show_remaining(next_player.ships)


if __name__ == '__main__':
    main()
