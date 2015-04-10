__author__ = 'donnywdavis'
__project__ = 'Battleship'

from random import randint

# Create our 10x10 grid for the game board
grid = []
for index in range(10):
    grid.append(["O"] * 10)

# Dictionary of ship details
ships = {
    "battleship": {
        "length": 4,
        "direction": "",
        "start": [],
        "end": []
    },
    "carrier": {
        "length": 6,
        "direction": "",
        "start": [],
        "end": []
    },
    "submarine": {
        "length": 3,
        "direction": "",
        "start": [],
        "end": []
    }
}

# Populate the ships onto the board
for ship in ships:
    ships[ship]["start"] = [randint(0, (len(board) - 1) - ships[ship]["length"]), randint(0, len(board) - 1)]
    if ships[ship]["start"][1] + ships[ship]["length"] > 10:
        ships[ship]["direction"] = "V"
        ships[ship]["end"] = [ships[ship]["start"][1], (ships[ship]["start"][0] + ships[ship]["length"]) - 1]
    else:
        ships[ship]["direction"] = "H"
        ships[ship]["end"] = [ships[ship]["start"][0], (ships[ship]["start"][1] + ships[ship]["length"]) - 1]


# Draw the board to the screen
def draw_board(board):
    for row in board:
        print(" ".join(row))


draw_board(grid)