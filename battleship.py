__author__ = 'donnywdavis'
__project__ = 'Battleship'

from random import randint
from game_board import GameBoard

print("Let's play Battleship!")

# Create our 10x10 grid for the game board
board = GameBoard(10, 6)

# Create our ships
board.add_ship("battleship", 4)
board.add_ship("carrier", 6)
board.add_ship("submarine", 3)
print(board.ship_positions)


# Check if a list of positions on the grid is already being used by another ship
def valid_ship_position(positions):
    if not positions:
        return False

    for thisShip in ships:
        for position in positions:
            if position in ships[thisShip]["positions"]:
                return False

    return True


# Dictionary of ship details
ships = {
    "battleship": {
        "length": 4,
        "positions": [],
        "hits": 0
    },
    "carrier": {
        "length": 6,
        "positions": [],
        "hits": 0
    },
    "submarine": {
        "length": 3,
        "positions": [],
        "hits": 0
    }
}

# Populate the ships onto the board
for ship in ships:
    shipPosition = []
    while not valid_ship_position(shipPosition):
        startPoint = [randint(0, (board.length - 1) - int(ships[ship]["length"])), randint(0, board.length - 1)]
        if startPoint[1] + ships[ship]["length"] > 10:
            shipPosition = [[x, startPoint[1]] for x in range(startPoint[0],
                                                              (int(ships[ship]["length"]) + startPoint[0]))]
        else:
            shipPosition = [[startPoint[0], y] for y in range(startPoint[1],
                                                              (int(ships[ship]["length"]) + startPoint[1]))]
    else:
        ships[ship]["positions"] = shipPosition


# Show position of ships after game is over
def show_ships():
    for ship in ships:
        for position in ships[ship]["positions"]:
            if not board.position_is_a_hit(position[0], position[1]):
                board.mark_ship_position(position[0], position[1])
    board.draw()


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