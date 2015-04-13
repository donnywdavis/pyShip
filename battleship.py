__author__ = 'donnywdavis'
__project__ = 'Battleship'

from random import randint

print("Let's play Battleship!")

# Create our 10x10 grid for the game board
grid = []
for index in range(10):
    grid.append(["O"] * 10)


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
    shipPosition = []
    while not valid_ship_position(shipPosition):
        startPoint = [randint(0, (len(grid) - 1) - int(ships[ship]["length"])), randint(0, len(grid) - 1)]
        if startPoint[1] + ships[ship]["length"] > 10:
            shipPosition = [[x, startPoint[1]] for x in range(startPoint[0],
                                                              (int(ships[ship]["length"]) + startPoint[0]))]
        else:
            shipPosition = [[startPoint[0], y] for y in range(startPoint[1],
                                                              (int(ships[ship]["length"]) + startPoint[1]))]
    else:
        ships[ship]["positions"] = shipPosition


# Draw the board to the screen
def draw_board(board):
    for row in board:
        print(" ".join(row))


draw_board(grid)

# Loop to try and sink a ship
turns = 1
maxTurns = 3
while turns <= maxTurns:
    row = input("Select a row: ")
    column = input("Select a column: ")
    selection = [(int(row) - 1), (int(column) - 1)]

    # Check for some errors
    if selection[0] < 1 or selection[0] > 9 or \
       selection[1] < 1 or selection[1] > 9:
        print("Invalid selection, try again.")
    elif grid[selection[0]][selection[1]] == "X":
        print("You've already selected that target")
    else:
        grid[selection[0]][selection[1]] = "X"
        draw_board(grid)
        turns += 1