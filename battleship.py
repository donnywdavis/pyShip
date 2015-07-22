__author__ = 'donnywdavis'
__project__ = 'pyShip'

from game_board_2 import GameBoard

if __name__ == "__main__":
    print("Let's play Battleship!")

    # Create our 10x10 grid for the game board
    board = GameBoard(10, 15)

    # Create our ships
    board.add_ship("battleship", 4)
    board.add_ship("carrier", 6)
    board.add_ship("submarine", 3)
    board.add_ship("destroyer", 2)
    board.draw()

    # Loop to try and sink a ship
    turn = 1
    while turn <= board.turns:
        print("\nTurn {0}".format(turn))
        row = input("Select a row: ")
        column = input("Select a column: ")
        selection = ((int(row) - 1), (int(column) - 1))

        # Check for some errors
        if not board.valid_selection(selection[0], selection[1]):
            print("\nInvalid selection, try again.")
        elif board.position_already_selected(selection[0], selection[1]):
            print("\nYou've already selected that target")
        else:
            if board.hit_detected(selection):
                board.mark_hit(selection[0], selection[1])
                if board.ships_sunk == len(board.ships):
                    print("\nYou Win! Game Over!")
                    board.show_all_ships()
                    break
            else:
                board.mark_miss(selection[0], selection[1])
            board.draw()
            turn += 1
    else:
        print("\nGame Over!")
        board.show_all_ships()