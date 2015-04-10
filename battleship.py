__author__ = 'donnywdavis'
__project__ = 'Battleship'

# Create our 10x10 grid for the game board
grid = []
for index in range(10):
    grid.append(["O"] * 10)

# List of ships for the board
shipsList = ["battleship", "carrier", "submarine"]
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


# Draw the board to the screen
def draw_board(board):
    for row in board:
        print(" ".join(row))


draw_board(grid)