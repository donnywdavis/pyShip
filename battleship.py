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
        "positions": []
    },
    "carrier": {
        "length": 6,
        "positions": []
    },
    "submarine": {
        "length": 3,
        "positions": []
    }
}

# Populate the ships onto the board
for ship in ships:
    startPoint = [randint(0, (len(board) - 1) - ships[ship]["length"]), randint(0, len(board) - 1)]
    if startPoint[1] + ships[ship]["length"] > 10:
        ships[ship]["positions"] = [[x, startPoint[1]] for x in range(startPoint[0], (ships[ship]["length"] + startPoint[0]))]
    else:
        ships[ship]["positions"] = [[startPoint[0], y] for y in range(startPoint[1], (ships[ship]["length"] + startPoint[1]))]


# Draw the board to the screen
def draw_board(board):
    for row in board:
        print(" ".join(row))


draw_board(grid)