__author__ = 'donnywdavis'
__project__ = 'Battleship'

from game_board import GameBoard

print("Let's play Battleship!")

# Create our 10x10 grid for the game board
board = GameBoard(10, 6)

# Create our ships
board.add_ship("battleship", 4)
board.add_ship("carrier", 6)
board.add_ship("submarine", 3)

board.draw()

# Loop to try and sink a ship
turn = 1
while turn <= board.turns:
    row = input("\nSelect a row: ")
    column = input("Select a column: ")
    selection = [(int(row) - 1), (int(column) - 1)]

    # Check for some errors
    if not board.valid_selection(selection[0], selection[1]):
        print("\nInvalid selection, try again.")
    elif board.position_already_selected(selection[0], selection[1]):
        print("\nYou've already selected that target")
    else:
        if board.hit_detected(selection):
            board.mark_hit(selection[0], selection[1])
        else:
            board.mark_miss(selection[0], selection[1])
        board.draw()
        turn += 1
else:
    print("\nGame Over!")
    board.show_all_ships()